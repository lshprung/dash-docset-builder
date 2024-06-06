# Dash Docset Builder

This is a repository providing sources building various Dash docsets using a Makefile. Supported docsets can be found under `./src/configs`. Simply pass the name of the docset as a target for the Makefile (e.g., `make GNU_Make`).

### Documentation

```
Usage: make DOCSET_NAME [BUILD_DIR=...]

  DOCSET_NAME must be a directory under ./src/configs.
  BUILD_DIR can be set to a directory to build under. The default is ./build

Other possible targets:
  archive                            - create .tgz archives for all docsets in BUILD_DIR (WIP)
  clean                              - remove all docsets and .tgz archives from BUILD_DIR
  $(BUILD_DIR)/$(DOCSET_NAME).docset - equivalent to DOCSET_NAME
  $(BUILD_DIR)/$(DOCSET_NAME).tgz    - create a .tgz archive of DOCSET_NAME
```
