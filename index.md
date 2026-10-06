# mkdocstrings-typescript

A Typescript handler for mkdocstrings.

Still in prototyping phase!

Feedback is welcome.

## Installation

```
pip install mkdocstrings-typescript
```

## Usage

Add these [TypeDoc](https://typedoc.org/) configuration files to your repository:

```
📁 ./
├── 📁 src/
│   └── 📁 package1/
├──  typedoc.base.json
└──  typedoc.json
```

typedoc.base.json

```
{
  "$schema": "https://typedoc.org/schema.json",
  "includeVersion": true
}
```

typedoc.json

```
{
  "extends": ["./typedoc.base.json"],
  "entryPointStrategy": "packages",
  "entryPoints": ["./src/*"]
}
```

Update the entrypoints to match your file layout so that TypeDoc can find your packages. See [TypeDoc's configuration documentation](https://typedoc.org/options/configuration/).

Then in each of your package, add this TypeDoc configuration file:

```
📁 ./
├── 📁 src/
│   └── 📁 package1/
│       └──  typedoc.json
├──  typedoc.base.json
└──  typedoc.json
```

typedoc.json

```
{
  "extends": ["../../typedoc.base.json"],
  "entryPointStrategy": "expand",
  "entryPoints": ["src/index.d.ts"]
}
```

Again, update entrypoints to match your file and package layout. See [TypeDoc's configuration documentation](https://typedoc.org/options/configuration/).

**Your packages must be built for TypeDoc to work.**

You are now able to use the TypeScript handler to inject API docs in your Markdown pages by referencing package names:

```
::: @owner/packageName
    handler: typescript
```

You can set the Typescript handler as default handler:

```
plugins:
- mkdocstrings:
    default_handler: typescript
```

By setting it as default handler you can omit it when injecting documentation:

```
::: @owner/packageName
```

## Sponsors
