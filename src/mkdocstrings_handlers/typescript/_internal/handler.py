# This module implements a handler for Typescript.

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any, ClassVar

from griffe_typedoc import ReflectionKind
from griffe_typedoc import load as load_typedoc
from mkdocs.exceptions import PluginError
from mkdocstrings import BaseHandler, CollectionError, CollectorItem, get_logger

from mkdocstrings_handlers.typescript._internal.config import TypescriptConfig, TypescriptOptions

if TYPE_CHECKING:
    from collections.abc import Mapping, MutableMapping

    from mkdocs.config.defaults import MkDocsConfig
    from mkdocstrings import HandlerOptions


_logger = get_logger(__name__)


class TypescriptHandler(BaseHandler):
    """The Typescript handler class."""

    name: ClassVar[str] = "typescript"
    """The handler's name."""

    domain: ClassVar[str] = "ts"
    """The cross-documentation domain/language for this handler."""

    enable_inventory: ClassVar[bool] = False
    """Whether this handler is interested in enabling the creation of the `objects.inv` Sphinx inventory file."""

    fallback_theme: ClassVar[str] = "material"
    """The theme to fallback to."""

    def __init__(self, config: TypescriptConfig, base_dir: Path, **kwargs: Any) -> None:
        """Initialize the handler.

        Parameters:
            config: The handler configuration.
            base_dir: The base directory of the project.
            **kwargs: Arguments passed to the parent constructor.
        """
        super().__init__(**kwargs)

        self.config = config
        """The handler configuration."""
        self.base_dir = base_dir
        """The base directory of the project."""
        self.global_options = config.options
        """The global configuration options."""

        self._collected: dict[str, CollectorItem] = {}

    def get_options(self, local_options: Mapping[str, Any]) -> HandlerOptions:
        """Get combined default, global and local options.

        Arguments:
            local_options: The local options.

        Returns:
            The combined options.
        """
        extra = {**self.global_options.get("extra", {}), **local_options.get("extra", {})}
        options = {**self.global_options, **local_options, "extra": extra}
        try:
            return TypescriptOptions.from_data(**options)
        except Exception as error:
            raise PluginError(f"Invalid options: {error}") from error

    def collect(self, identifier: str, options: TypescriptOptions) -> CollectorItem:
        """Collect data given an identifier and selection configuration."""
        # If we are in fallback mode, we don't want to collect anything.
        if options == {}:
            raise CollectionError("Fallback mode is not supported")

        # Split the identifier into package and path.
        try:
            package, path = identifier.split("::", 1)
        except ValueError:
            package, path = identifier, ""

        # Load the data if not already collected.
        if package not in self._collected:
            data = load_typedoc(["typedoc"])
            self._collected[data.name] = data
            if data.kind is ReflectionKind.PROJECT:
                self._collected.update({module.name: module for module in data.children})
            _logger.debug(f"Collected {', '.join(self._collected.keys())}")

        # Find the object in the collected data.
        if package in self._collected:
            for child in self._collected[package].children:
                if child.kind is ReflectionKind.MODULE and child.name == "index":
                    package_obj = child
                    break
            else:
                package_obj = self._collected[package]

            # If no path, return the package object.
            if not path:
                return package_obj

            # Find the object in the package.
            parts = path.split(".")
            obj = package_obj
            while parts:
                part = parts.pop(0)
                for child in obj.children:
                    if child.name == part:
                        obj = child
                        break
                else:
                    raise CollectionError(f"Could not find {path} in {package}")
            return obj

        # If we couldn't find the object, raise an error.
        raise CollectionError(f"Could not collect {identifier}")

    def render(self, data: CollectorItem, options: TypescriptOptions) -> str:
        """Render a template using provided data and configuration options."""
        template = self.env.get_template("dispatch.html.jinja")
        return template.render(
            config=options,
            obj=data,
            heading_level=options.heading_level,
            root=True,
        )

    def get_aliases(self, identifier: str) -> tuple[str, ...]:
        """Get aliases for a given identifier."""
        try:
            data = self._collected[identifier]
        except KeyError:
            return ()
        return (data.path,)

    def update_env(self, config: dict) -> None:  # noqa: ARG002
        """Update the Jinja environment with any custom settings/filters/options for this handler.

        Parameters:
            config: MkDocs configuration, read from `mkdocs.yml`.
        """
        self.env.trim_blocks = True
        self.env.lstrip_blocks = True
        self.env.keep_trailing_newline = False


def get_handler(
    handler_config: MutableMapping[str, Any],
    tool_config: MkDocsConfig,
    **kwargs: Any,
) -> TypescriptHandler:
    """Simply return an instance of `TypescriptHandler`.

    Arguments:
        handler_config: The handler configuration.
        tool_config: The tool (SSG) configuration.

    Returns:
        An instance of `TypescriptHandler`.
    """
    base_dir = Path(tool_config.config_file_path or "./mkdocs.yml").parent
    return TypescriptHandler(
        config=TypescriptConfig.from_data(**handler_config),
        base_dir=base_dir,
        **kwargs,
    )
