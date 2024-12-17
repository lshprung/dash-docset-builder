# Dash Docset Builder

This is a repository providing sources building various [Dash](https://kapeli.com/dash) docsets using a Makefile. Supported docsets can be found as a submodule under `./src/configs`. Simply pass the name of the docset as a target for the Makefile (e.g., `make GNU_Make`).

### Documentation

<!-- TODO:
  BUILD_FROM_SOURCE - compile the documentation from upstream, rather than downloading from a prebuild source (this is the default behavior for many docset generation scripts)
-->

```
Usage: make DOCSET_NAME [BUILD_DIR=...] [NO_CSS=yes] [LOCALE=...] [VERSION=...]

  DOCSET_NAME must be a directory under ./src/configs.
  BUILD_DIR   can be set to a directory to build under. The default is ./build.
  NO_CSS      if set to `yes`, build with stylesheets disabled.
  LOCALE      specify a locale to build for (see below table for more details).
  VERSION     specify an upstream version to build from.

Other possible targets:
  archive                            - create .tgz archives for all docsets in BUILD_DIR
  clean                              - remove all docsets and .tgz archives from BUILD_DIR
  $(BUILD_DIR)/$(DOCSET_NAME).docset - equivalent to DOCSET_NAME
  $(BUILD_DIR)/$(DOCSET_NAME).tgz    - create a .tgz archive of DOCSET_NAME
```

#### Supported Definitions

This table shows which supported docsets support which options. All targets support the setting of DOCSET_NAME and BUILD_DIR.

|                                                      |LOCALE|NO_CSS|VERSION|
|------------------------------------------------------|------|------|-------|
|[debmake](https://salsa.debian.org/debian/debmake)    |✓ (see [here](./src/configs/debmake/README.md))||✓|
|[flex](https://github.com/westes/flex)                |      |      |✓      |
|[GNU_Autoconf](https://www.gnu.org/software/autoconf/)|      |      |✓      |
|[GNU_Autoconf_Archive](https://www.gnu.org/software/autoconf-archive/)|||✓|
|[GNU_Automake](https://www.gnu.org/software/automake/)|      |      |       |
|[GNU_Bash](https://www.gnu.org/software/bash/)        |      |      |       |
|[GNU_Bison](https://www.gnu.org/software/bison/)      |      |      |       |
|[GNU_Make](http://www.gnu.org/software/make/)         |      |✓     |       |
|[ncurses](https://invisible-island.net/ncurses/)      |      |      |✓      |

### Build Requirements

This table shows the dependencies for each supported docset. Additionally, all docsets depend on a POSIX-compliant shell (e.g. [bash](https://www.gnu.org/software/bash/)), [make](https://www.gnu.org/software/make/), and [sqlite3](https://www.sqlite.org/index.html).

| |[curl](https://curl.se/)|[po4a](https://po4a.org/)|[pup](https://github.com/ericchiang/pup)|[texinfo](https://www.gnu.org/software/texinfo/)|
|-|------------------------|-------------------------|----------------------------------------|------------------------------------------------|
|[debmake](https://salsa.debian.org/debian/debmake)                    |✓|✓| | |
|[flex](https://github.com/westes/flex)                                |✓| |✓|✓|
|[GNU_Autoconf](https://www.gnu.org/software/autoconf/)                |✓| |✓| |
|[GNU_Autoconf_Archive](https://www.gnu.org/software/autoconf-archive/)|✓| |✓|✓|
|[GNU_Automake](https://www.gnu.org/software/automake/)                |✓| |✓| | 
|[GNU_Bash](https://www.gnu.org/software/bash/)                        |✓| |✓| | 
|[GNU_Bison](https://www.gnu.org/software/bison/)                      |✓| |✓| |
|[GNU_Make](http://www.gnu.org/software/make/)                         |✓| |✓| |
|[ncurses](https://invisible-island.net/ncurses/)                      |✓| |✓| |

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
