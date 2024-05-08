"""This module implements a handler for the Typescript language."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, ClassVar, Mapping, MutableMapping

from mkdocstrings.handlers.base import BaseHandler, CollectorItem
from mkdocstrings.loggers import get_logger

if TYPE_CHECKING:
    from markdown import Markdown


logger = get_logger(__name__)


class TypescriptHandler(BaseHandler):
    """The Typescript handler class."""

    domain: str = "typescript"
    """The cross-documentation domain/language for this handler."""

    enable_inventory: bool = False
    """Whether this handler is interested in enabling the creation of the `objects.inv` Sphinx inventory file."""

    fallback_theme = "material"
    """The theme to fallback to."""

    fallback_config: ClassVar[dict] = {"fallback": True}
    """The configuration used to collect item during autorefs fallback."""

    default_config: ClassVar[dict] = {
        "base_file_path": ".",
        "docstring_style": "google",
        "docstring_options": {},
        "show_symbol_type_heading": False,
        "show_symbol_type_toc": False,
        "show_root_heading": False,
        "show_root_toc_entry": True,
        "show_root_full_path": True,
        "show_root_members_full_path": False,
        "show_object_full_path": False,
        "show_category_heading": False,
        "show_if_no_docstring": False,
        "show_signature": True,
        "show_signature_annotations": False,
        "signature_crossrefs": False,
        "separate_signature": False,
        "line_length": 60,
        "merge_init_into_class": False,
        "show_docstring_attributes": True,
        "show_docstring_functions": True,
        "show_docstring_classes": True,
        "show_docstring_modules": True,
        "show_docstring_description": True,
        "show_docstring_examples": True,
        "show_docstring_other_parameters": True,
        "show_docstring_parameters": True,
        "show_docstring_raises": True,
        "show_docstring_receives": True,
        "show_docstring_returns": True,
        "show_docstring_warns": True,
        "show_docstring_yields": True,
        "show_source": True,
        "show_bases": True,
        "show_submodules": False,
        "group_by_category": True,
        "heading_level": 2,
        "members_order": "alphabetical",
        "docstring_section_style": "table",
        "members": None,
        "inherited_members": False,
        "filters": ["!^_[^_]"],
        "annotations_path": "brief",
        "preload_modules": None,
        "allow_inspection": True,
        "summary": False,
        "unwrap_annotated": False,
        "parameter_headings": False,
    }
    """The default configuration options.

    Option | Type | Description | Default
    ------ | ---- | ----------- | -------
    **`show_root_heading`** | `bool` | Show the heading of the object at the root of the documentation tree. | `False`
    **`show_root_toc_entry`** | `bool` | If the root heading is not shown, at least add a ToC entry for it. | `True`
    **`heading_level`** | `int` | The initial heading level to use. | `2`
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the handler.

        Parameters:
            *args: Passed to the [base handler][mkdocstrings.handlers.base import BaseHandler].
            **kwargs: Passed to the [base handler][mkdocstrings.handlers.base import BaseHandler].
        """
        kwargs.pop("config_file_path", None)
        super().__init__(*args, **kwargs)
        self._collected: dict[str, CollectorItem] = {}

    def collect(self, identifier: str, config: MutableMapping[str, Any]) -> CollectorItem:  # noqa: ARG002
        """Collect data given an identifier and selection configuration.

        In the implementation, you typically call a subprocess that returns JSON, and load that JSON again into
        a Python dictionary for example, though the implementation is completely free.

        Parameters:
            identifier: An identifier that was found in a markdown document for which to collect data. For example,
                in Python, it would be 'mkdocstrings.handlers' to collect documentation about the handlers module.
                It can be anything that you can feed to the tool of your choice.
            config: All configuration options for this handler either defined globally in `mkdocs.yml` or
                locally overridden in an identifier block by the user.

        Returns:
            Anything you want, as long as you can feed it to the `render` method.
        """
        return {"identifier": identifier}

    def render(self, data: CollectorItem, config: Mapping[str, Any]) -> str:  # noqa: ARG002
        """Render a template using provided data and configuration options.

        Parameters:
            data: The data to render that was collected above in `collect()`.
            config: All configuration options for this handler either defined globally in `mkdocs.yml` or
                locally overridden in an identifier block by the user.

        Returns:
            The rendered template as HTML.
        """
        return (
            f"<i><b><code>::: {data['identifier']}</code></b><br>The public version of mkdocstrings-typescript is a no-op "
            "and exist only to allow building docs without errors. Please rely on docs preview in CI.</i>"
        )

    def update_env(self, md: Markdown, config: dict) -> None:
        """Update the Jinja environment with any custom settings/filters/options for this handler.

        Parameters:
            md: The Markdown instance. Useful to add functions able to convert Markdown into the environment filters.
            config: Configuration options for `mkdocs` and `mkdocstrings`, read from `mkdocs.yml`. See the source code
                of [mkdocstrings.plugin.MkdocstringsPlugin.on_config][] to see what's in this dictionary.
        """
        super().update_env(md, config)  # Add some mkdocstrings default filters such as highlight and convert_markdown
        self.env.trim_blocks = True
        self.env.lstrip_blocks = True
        self.env.keep_trailing_newline = False


def get_handler(
    theme: str,
    custom_templates: str | None = None,
    config_file_path: str | None = None,
    **config: Any,  # noqa: ARG001
) -> TypescriptHandler:
    """Simply return an instance of `TypescriptHandler`.

    Parameters:
        theme: The theme to use when rendering contents.
        custom_templates: Directory containing custom templates.
        config_file_path: The MkDocs configuration file path.
        **config: Configuration passed to the handler.

    Returns:
        An instance of the handler.
    """
    return TypescriptHandler(
        handler="typescript",
        theme=theme,
        custom_templates=custom_templates,
        config_file_path=config_file_path,
    )
