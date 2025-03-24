"""Typescript handler for mkdocstrings."""

from mkdocstrings_handlers.typescript._internal.config import (
    TypescriptConfig,
    TypescriptInputConfig,
    TypescriptInputOptions,
    TypescriptOptions,
)
from mkdocstrings_handlers.typescript._internal.handler import TypescriptHandler, get_handler

__all__ = [
    "TypescriptConfig",
    "TypescriptHandler",
    "TypescriptInputConfig",
    "TypescriptInputOptions",
    "TypescriptOptions",
    "get_handler",
]
