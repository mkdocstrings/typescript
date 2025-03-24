# Customization

It is possible to customize the output of the generated documentation with CSS and/or by overriding templates.

## CSS classes

Our templates add [CSS](https://www.w3schools.com/Css/) classes to many HTML elements to make it possible for users to customize the resulting look and feel.

To add CSS rules and style mkdocstrings' output, put them in a CSS file in your docs folder, for example in `docs/css/mkdocstrings.css`, and reference this file in [MkDocs' `extra_css` configuration option](https://www.mkdocs.org/user-guide/configuration/#extra_css):

```yaml title="mkdocs.yml"
extra_css:
- css/mkdocstrings.css
```

Example:

```css title="docs/css/mkdocstrings.css"
.doc-section-title {
  font-weight: bold;
}
```

## Symbol types

### Colors

You can customize the colors of the symbol types (see [`show_symbol_type_heading`][show_symbol_type_heading] and [`show_symbol_type_toc`][show_symbol_type_toc]) by overriding the values of our CSS variables, for example:

```css title="docs/css/mkdocstrings.css"
[data-md-color-scheme="default"] {
  --doc-symbol-ts-accessor-fg-color: #6f42c1
  --doc-symbol-ts-attribute-fg-color: #6f42c1
  --doc-symbol-ts-class-fg-color: #22863a
  --doc-symbol-ts-constructor-fg-color: #1f66ff
  --doc-symbol-ts-data-fg-color: #0366d6
  --doc-symbol-ts-enum-fg-color: #6f42c1
  --doc-symbol-ts-enum_member-fg-color: #f0ad4e
  --doc-symbol-ts-interface-fg-color: #6f42c1
  --doc-symbol-ts-method-fg-color: #0366d6
  --doc-symbol-ts-module-fg-color: #0366d6
  --doc-symbol-ts-namespace-fg-color: #0366d6
  --doc-symbol-ts-parameter-fg-color: #e36209
  --doc-symbol-ts-project-fg-color: #24292f
  --doc-symbol-ts-property-fg-color: #6f42c1
  --doc-symbol-ts-type-fg-color: #6f42c1
  --doc-symbol-ts-type_alias-fg-color: #6f42c1
  --doc-symbol-ts-variable-fg-color: #e36209

  --doc-symbol-ts-accessor-bg-color: #6f42c11a
  --doc-symbol-ts-attribute-bg-color: #6f42c11a
  --doc-symbol-ts-class-bg-color: #22863a1a
  --doc-symbol-ts-constructor-bg-color: #1f66ff1a
  --doc-symbol-ts-data-bg-color: #0366d61a
  --doc-symbol-ts-enum-bg-color: #6f42c11a
  --doc-symbol-ts-enum_member-bg-color: #f0ad4e1a
  --doc-symbol-ts-interface-bg-color: #6f42c11a
  --doc-symbol-ts-method-bg-color: #0366d61a
  --doc-symbol-ts-module-bg-color: #0366d61a
  --doc-symbol-ts-namespace-bg-color: #0366d61a
  --doc-symbol-ts-parameter-bg-color: #e362091a
  --doc-symbol-ts-project-bg-color: #24292f1a
  --doc-symbol-ts-property-bg-color: #6f42c11a
  --doc-symbol-ts-type-bg-color: #6f42c11a
  --doc-symbol-ts-type_alias-bg-color: #6f42c11a
  --doc-symbol-ts-variable-bg-color: #e362091a
}

[data-md-color-scheme="slate"] {
  --doc-symbol-ts-accessor-fg-color: #d4a5f0
  --doc-symbol-ts-attribute-fg-color: #d4a5f0
  --doc-symbol-ts-class-fg-color: #78e7d1
  --doc-symbol-ts-constructor-fg-color: #6ba3ff
  --doc-symbol-ts-data-fg-color: #58a6ff
  --doc-symbol-ts-enum-fg-color: #d4a5f0
  --doc-symbol-ts-enum_member-fg-color: #ffb864
  --doc-symbol-ts-interface-fg-color: #d4a5f0
  --doc-symbol-ts-method-fg-color: #58a6ff
  --doc-symbol-ts-module-fg-color: #58a6ff
  --doc-symbol-ts-namespace-fg-color: #58a6ff
  --doc-symbol-ts-parameter-fg-color: #f4a261
  --doc-symbol-ts-project-fg-color: #e1e4e8
  --doc-symbol-ts-property-fg-color: #d4a5f0
  --doc-symbol-ts-type-fg-color: #d4a5f0
  --doc-symbol-ts-type_alias-fg-color: #d4a5f0
  --doc-symbol-ts-variable-fg-color: #f4a261

  --doc-symbol-ts-accessor-bg-color: #d4a5f01a
  --doc-symbol-ts-attribute-bg-color: #d4a5f01a
  --doc-symbol-ts-class-bg-color: #78e7d11a
  --doc-symbol-ts-constructor-bg-color: #6ba3ff1a
  --doc-symbol-ts-data-bg-color: #58a6ff1a
  --doc-symbol-ts-enum-bg-color: #d4a5f01a
  --doc-symbol-ts-enum_member-bg-color: #ffb8641a
  --doc-symbol-ts-interface-bg-color: #d4a5f01a
  --doc-symbol-ts-method-bg-color: #58a6ff1a
  --doc-symbol-ts-module-bg-color: #58a6ff1a
  --doc-symbol-ts-namespace-bg-color: #58a6ff1a
  --doc-symbol-ts-parameter-bg-color: #f4a2611a
  --doc-symbol-ts-project-bg-color: #e1e4e81a
  --doc-symbol-ts-property-bg-color: #d4a5f01a
  --doc-symbol-ts-type-bg-color: #d4a5f01a
  --doc-symbol-ts-type_alias-bg-color: #d4a5f01a
  --doc-symbol-ts-variable-bg-color: #f4a2611a
}
```

The `[data-md-color-scheme="*"]` selectors work with the [Material for MkDocs] theme. If you are using another theme, adapt the selectors to this theme if it supports light and dark themes, otherwise just override the variables at root level:

```css title="docs/css/mkdocstrings.css"
:root {
  --doc-symbol-ts-data-fg-color: #d1b619;
  --doc-symbol-ts-data-bg-color: #d1b6191a;
}
```

/// admonition | Preview
    type: preview

<div id="preview-symbol-colors">
  <style>
    [data-md-color-scheme="default"] #preview-symbol-colors {
      --doc-symbol-ts-data-fg-color: #d1b619;
      --doc-symbol-ts-data-bg-color: #d1b6191a;
    }

    [data-md-color-scheme="slate"] #preview-symbol-colors {
      --doc-symbol-ts-data-fg-color: #46c2cb;
      --doc-symbol-ts-data-bg-color: #46c2cb1a;
    }
  </style>
  <p>
    Try cycling through the themes to see the colors for each theme:
    <code class="doc-symbol doc-symbol-ts-data"></code
  </p>
</div>

///

### Names

You can also change the actual symbol names. For example, to use single letters instead of truncated types:

```css title="docs/css/mkdocstrings.css"
.doc-symbol-ts-data::after {
  content: "D";
}
```

/// admonition | Preview
    type: preview

<div id="preview-symbol-names">
  <style>
    #preview-symbol-names .doc-symbol-ts-data::after {
      content: "D";
    }
  </style>
  <ul>
    <li>Data: <code class="doc-symbol doc-symbol-ts-data"></code></li>
  </ul>
</div>

///

## Templates

Templates are organized into the following tree:

```python exec="1" result="tree"
from pathlib import Path

basedir = "src/mkdocstrings_handlers/typescript/templates/material"
print("theme/")
for filepath in sorted(path for path in Path(basedir).rglob("*") if "_base" not in str(path) and path.suffix != ".css"):
    print(
        "    " * (len(filepath.relative_to(basedir).parent.parts) + 1)
        + filepath.name
        + ("/" if filepath.is_dir() else "")
    )
```

See them [in the repository](https://github.com/mkdocstrings/typescript/tree/main/src/mkdocstrings_handlers/typescript/templates/).
See the general *mkdocstrings* documentation to learn how to override them: https://mkdocstrings.github.io/theming/#templates.

Each one of these templates extends a base version in `theme/_base`. Example:

```html+jinja title="theme/data.html.jinja"
{% extends "_base/data.html.jinja" %}
```

Some of these templates define [Jinja blocks](https://jinja.palletsprojects.com/en/3.0.x/templates/#template-inheritance).
allowing to customize only *parts* of a template
without having to fully copy-paste it into your project:

```jinja title="templates/theme/data.html"
{% extends "_base/data.html" %}
{% block contents scoped %}
  {{ block.super }}
  Additional contents
{% endblock contents %}
```
