# mkdocstrings-typescript

[![ci](https://github.com/mkdocstrings/typescript/workflows/ci/badge.svg)](https://github.com/mkdocstrings/typescript/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs-708FCC.svg?style=flat)](https://mkdocstrings.github.io/typescript/)
[![pypi version](https://img.shields.io/pypi/v/mkdocstrings-typescript.svg)](https://pypi.org/project/mkdocstrings-typescript/)
[![gitter](https://badges.gitter.im/join%20chat.svg)](https://app.gitter.im/#/room/#typescript:gitter.im)

A Typescript handler for mkdocstrings.

WARNING: **Still in prototyping phase!**
Feedback is welcome.

## Installation

```bash
pip install mkdocstrings-typescript
```

## Usage

Add these [TypeDoc](https://typedoc.org/) configuration files to your repository:

```tree hl_lines="4 5"
./
    src/
        package1/
    typedoc.base.json
    typedoc.json
```

```json title="typedoc.base.json"
{
  "$schema": "https://typedoc.org/schema.json",
  "includeVersion": true
}
```

```json title="typedoc.json"
{
  "extends": ["./typedoc.base.json"],
  "entryPointStrategy": "packages",
  "entryPoints": ["./src/*"]
}
```

Update the entrypoints to match your file layout so that TypeDoc can find your packages. See [TypeDoc's configuration documentation](https://typedoc.org/options/configuration/).

Then in each of your package, add this TypeDoc configuration file:

```tree hl_lines="4"
./
    src/
        package1/
            typedoc.json
    typedoc.base.json
    typedoc.json
```

```json title="typedoc.json"
{
  "extends": ["../../typedoc.base.json"],
  "entryPointStrategy": "expand",
  "entryPoints": ["src/index.d.ts"]
}
```

Again, update entrypoints to match your file and package layout. See [TypeDoc's configuration documentation](https://typedoc.org/options/configuration/).

**Your packages must be built for TypeDoc to work.**

You are now able to use the TypeScript handler to inject API docs in your Markdown pages by referencing package names:

```md
::: @owner/packageName
    handler: typescript
```

You can set the Typescript handler as default handler:

```yaml
plugins:
- mkdocstrings:
    default_handler: typescript
```

By setting it as default handler you can omit it when injecting documentation:

```md
::: @owner/packageName
```
