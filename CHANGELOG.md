# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
## [0.1.0](https://github.com/mkdocstrings/typescript/releases/tag/0.1.0) - 2025-03-24

<small>[Compare with 0.0.1](https://github.com/mkdocstrings/typescript/compare/0.0.1...0.1.0)</small>

**The project gets released to everyone!**

### Build

- Depend on griffe-typedoc 0.1 ([7d09f9a](https://github.com/mkdocstrings/typescript/commit/7d09f9a380a844296739e7eaad3554095af0400a) by Timothée Mazzucotelli).
- Require Python 3.10 minimum ([1e5c521](https://github.com/mkdocstrings/typescript/commit/1e5c52140635bbd32d03aeaf7da6badeedef29c8) by Timothée Mazzucotelli).
- Depend on mkdocstrings 0.28.3 ([c5bf04e](https://github.com/mkdocstrings/typescript/commit/c5bf04e063f12a0cf94e8164af29b9b986acb887) by Timothée Mazzucotelli).

### Features

- Declare and use symbols for all kinds of objects ([a2392aa](https://github.com/mkdocstrings/typescript/commit/a2392aaa8db99b468d70b7280584b96eb12c7ad9) by Timothée Mazzucotelli).
- Support specifying an object path ([9b32feb](https://github.com/mkdocstrings/typescript/commit/9b32febbe0ad880eae3117d631db481ff344d16f) by Timothée Mazzucotelli). [Issue-22](https://github.com/mkdocstrings/typescript/issues/22)
- Pass symbol map to `markdown` method of objects, to allow generating autorefs ([3324c2a](https://github.com/mkdocstrings/typescript/commit/3324c2adc62be8e44106f89169822e360d64c35e) by Timothée Mazzucotelli). [Issue-5](https://github.com/mkdocstrings/typescript/issues/5)
- Suffix templates with jinja extension, add templates for enum, enum member, class and constructor ([49fcd56](https://github.com/mkdocstrings/typescript/commit/49fcd566b6d4e74f2bd4681829181be69f8edd05) by Timothée Mazzucotelli). [Issue-3](https://github.com/mkdocstrings/typescript/issues/3), [Issue-4](https://github.com/mkdocstrings/typescript/issues/4)
- Generate project with gh:mkdocstrings/handler-template Copier template ([79a9244](https://github.com/mkdocstrings/typescript/commit/79a924496d190642e58d127f8b29640c81041c3f) by Timothée Mazzucotelli).

### Bug Fixes

- Add templates for projects ([9648248](https://github.com/mkdocstrings/typescript/commit/9648248efac8d1b0ecccce6bdec5e7882eaabdc8) by Timothée Mazzucotelli).
- Add templates for namespaces ([277af0f](https://github.com/mkdocstrings/typescript/commit/277af0f7deab48c1d492e8e109c25a978bb43434) by Timothée Mazzucotelli). [Issue-mkdocstrings/typescript#16](https://github.com/mkdocstrings/typescript/issues/16)
- Add templates for accessors ([57405cb](https://github.com/mkdocstrings/typescript/commit/57405cba0a2652cf21acdb89865cee29fbfff0ca) by Timothée Mazzucotelli). [Issue-13](https://github.com/mkdocstrings/typescript/issues/13)
- Collect project anyway, not just its children ([3895e88](https://github.com/mkdocstrings/typescript/commit/3895e8812a731d075e5fbba4c771ecaebaa6af65) by Timothée Mazzucotelli). [Issue-2](https://github.com/mkdocstrings/typescript/issues/2)

### Code Refactoring

- Import from top-level mkdocstrings module ([a16da56](https://github.com/mkdocstrings/typescript/commit/a16da568a1d0cbd3d3099b62569211086a071313) by Timothée Mazzucotelli).
- Improve support for signatures rendering (wip) ([bcbc314](https://github.com/mkdocstrings/typescript/commit/bcbc314203c6b9da24ca46a3db1536a61cffb3f3) by Timothée Mazzucotelli).

## [0.0.1](https://github.com/mkdocstrings/typescript/releases/tag/0.0.1) - 2024-05-08

<small>[Compare with first commit](https://github.com/mkdocstrings/typescript/compare/00cd6f133945a103d9e71cc6b413c0738a07f9d1...0.0.1)</small>

### Build

- Release no-op version ([04dfa30](https://github.com/mkdocstrings/typescript/commit/04dfa30942014a113806f9ad5981718a620a6532) by Timothée Mazzucotelli).
