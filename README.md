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
|[debmake](https://salsa.debian.org/debian/debmake) ([latest docset release](https://github.com/lshprung/debmake-dash-docset/releases/latest))|✓ (see [here](./src/configs/debmake/README.md))||✓|
|[flex](https://github.com/westes/flex) ([latest docset release](https://github.com/lshprung/flex-dash-docset/releases/latest)|||✓|
|[glibc (GNU C Library)](https://www.gnu.org/software/libc/libc.html) ([latest docset release](https://github.com/lshprung/gnu-libc-dash-docset/releases/latest))|||✓|
|[GNU_Autoconf](https://www.gnu.org/software/autoconf/) ([latest docset release](https://github.com/lshprung/gnu-autoconf-dash-docset/releases/latest)|||✓|
|[GNU_Autoconf_Archive](https://www.gnu.org/software/autoconf-archive/) ([latest docset release](https://github.com/lshprung/gnu-autoconf-archive-dash-docset/releases/latest)|||✓|
|[GNU_Automake](https://www.gnu.org/software/automake/) ([latest docset release](https://github.com/lshprung/gnu-automake-dash-docset/releases/latest)||||
|[GNU_Bash](https://www.gnu.org/software/bash/) ([latest docset release](https://github.com/lshprung/gnu-bash-dash-docset/releases/latest)||||
|[GNU_Bison](https://www.gnu.org/software/bison/) ([latest docset release](https://github.com/lshprung/gnu-bison-dash-docset/releases/latest)||||
|[GNU_Coding_Standards](https://savannah.gnu.org/projects/gnustandards) ([latest docset release](https://github.com/lshprung/gnu-coding-standards-dash-docset/releases/latest)||||
|[GNU_Coreutils](https://www.gnu.org/software/coreutils) ([latest docset release](https://github.com/lshprung/gnu-coreutils-dash-docset/releases/latest)||||
|[GNU_Guix](https://guix.gnu.org/) ([latest docset release](https://github.com/lshprung/gnu-guix-dash-docset/releases/latest)|||✓|
|[GNU_Libtool](https://www.gnu.org/software/libtool/) ([latest docset release](https://github.com/lshprung/gnu-libtool-dash-docset/releases/latest)||||
|[GNU_Make](http://www.gnu.org/software/make/) ([latest docset release](https://github.com/lshprung/gnu-make-dash-docset/releases/latest)||✓||
|[ncurses](https://invisible-island.net/ncurses/) ([latest docset release](https://github.com/lshprung/ncurses-dash-docset/releases/latest)|||✓|

### Build Requirements

All docsets depend on [python3](https://www.python.org/) and [make](https://www.gnu.org/software/make/) to build. Some additional dependencies may be required if the docset is being built from source (rather than from an html source)

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
