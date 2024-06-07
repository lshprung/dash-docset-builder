# Dash Docset Builder

This is a repository providing sources building various Dash docsets using a Makefile. Supported docsets can be found as a submodule under `./src/configs`. Simply pass the name of the docset as a target for the Makefile (e.g., `make GNU_Make`).

### Documentation

```
Usage: make DOCSET_NAME [BUILD_DIR=...] [NO_CSS=yes] [LOCALE=...]

  DOCSET_NAME must be a directory under ./src/configs.
  BUILD_DIR   can be set to a directory to build under. The default is ./build
  NO_CSS      if set to `yes`, build with stylesheets disabled.
  LOCALE      specify a locale to build for (see below table for more details).

Other possible targets:
  archive                            - create .tgz archives for all docsets in BUILD_DIR
  clean                              - remove all docsets and .tgz archives from BUILD_DIR
  $(BUILD_DIR)/$(DOCSET_NAME).docset - equivalent to DOCSET_NAME
  $(BUILD_DIR)/$(DOCSET_NAME).tgz    - create a .tgz archive of DOCSET_NAME
```

#### Supported Definitions

This table shows which supported docsets support which options. All targets support the setting of DOCSET_NAME and BUILD_DIR.

|                                                  |NO_CSS|LOCALE|
|--------------------------------------------------|------|------|
|[GNU_Make](http://www.gnu.org/software/make/)     |✓     |      |
|[debmake](https://salsa.debian.org/debian/debmake)|      |✓ (see [here](./src/configs/debmake/README.md))|

### Build Requirements

This table shows the dependencies for each supported docset. Additionally, all docsets depend on a POSIX-compliant shell (e.g. [bash](https://www.gnu.org/software/bash/)), [make](https://www.gnu.org/software/make/), and [sqlite3](https://www.sqlite.org/index.html).

| |[curl](https://curl.se/)|[po4a](https://po4a.org/)|[pup](https://github.com/ericchiang/pup)|
|-|------------------------|-------------------------|----------------------------------------|
|[GNU_Make](http://www.gnu.org/software/make/)     |✓|✓| |
|[debmake](https://salsa.debian.org/debian/debmake)|✓| |✓|

### Project Structure

```
.
├── src
│   ├── configs    - supported docsets, including metadata and build scripts
│   └── scripts    - general purpose scripts
└── tmp            - intermediate sources (e.g., upstream sources are downloaded to here)
```

### Credits

- [Louie Shprung](https://github.com/lshprung/)
- Design is based on [benzado](https://github.com/benzado)'s [gnu-make-dash-docset](https://github.com/benzado/gnu-make-dash-docset)
