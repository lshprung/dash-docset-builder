# Dash Docset Builder

This is a repository providing sources building various Dash docsets using a Makefile. Supported docsets can be found under `./configs`.

### Documentation

```
Usage: make DOCSET_NAME=... [BUILD_DIR=...]

  DOCSET_NAME must be set to the name of a directory under ./configs.
  BUILD_DIR can be set to a directory to build under. The default is the project root

Examples:
  make DOCSET_NAME=GNU_Make
  make DOCSET_NAME=GNU_Make BUILD_DIR=build/
```
