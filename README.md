# Dash Docset Builder

This is a repository providing common sources for building various 
[Dash](https://kapeli.com/dash) docsets, as required by the python packages 
listed below.

|                                                     |Upstream|Latest Release|
|-----------------------------------------------------|--------|--------------|
|[debmake](https://github.com/lshprung/debmake-dash-docset)|[link](https://salsa.debian.org/debian/debmake)|[link](https://github.com/lshprung/debmake-dash-docset/releases/latest)|
|[flex](https://github.com/lshprung/flex-dash-docset)|[link](https://github.com/westes/flex)|[link](https://github.com/lshprung/flex-dash-docset/releases/latest)|
|[glibc (GNU C Library](https://github.com/lshprung/gnu-libc-dash-docset)|[link](https://www.gnu.org/software/libc/libc.html)|[link](https://github.com/lshprung/gnu-libc-dash-docset/releases/latest)|
|[GNU Autoconf](https://github.com/lshprung/gnu-autoconf-dash-docset)|[link](https://www.gnu.org/software/autoconf/)|[link](https://github.com/lshprung/gnu-autoconf-dash-docset/releases/latest)|
|[GNU Autoconf Archive](https://github.com/lshprung/gnu-autoconf-archive-dash-docset)|[link](https://www.gnu.org/software/autoconf-archive/)|[link](https://github.com/lshprung/gnu-autoconf-archive-dash-docset/releases/latest)|
|[GNU Automake](https://github.com/lshprung/gnu-automake-dash-docset)|[link](https://www.gnu.org/software/automake/)|[link](https://github.com/lshprung/gnu-automake-dash-docset/releases/latest)|
|[GNU Bash](https://github.com/lshprung/gnu-bash-dash-docset)|[link](https://www.gnu.org/software/bash/)|[link](https://github.com/lshprung/gnu-bash-dash-docset/releases/latest)|
|[GNU Bison](https://github.com/lshprung/gnu-bison-dash-docset)|[link](https://www.gnu.org/software/bison/)|[link](https://github.com/lshprung/gnu-bison-dash-docset/releases/latest)|
|[GNU Coding Standards](https://github.com/lshprung/gnu-coding-standards-dash-docset)|[link](https://savannah.gnu.org/projects/gnustandards)|[link](https://github.com/lshprung/gnu-coding-standards-dash-docset/releases/latest)|
|[GNU Coreutils](https://github.com/lshprung/gnu-coreutils-dash-docset)|[link](https://www.gnu.org/software/coreutils)|[link](https://github.com/lshprung/gnu-coreutils-dash-docset/releases/latest)|
|[GNU Guix](https://github.com/lshprung/gnu-guix-dash-docset)|[link](https://guix.gnu.org/)|[link](https://github.com/lshprung/gnu-guix-dash-docset/releases/latest)|
|[GNU Libtool](https://github.com/lshprung/gnu-libtool-dash-docset)|[link](https://www.gnu.org/software/libtool/)|[link](https://github.com/lshprung/gnu-libtool-dash-docset/releases/latest)|
|[GNU Make](https://github.com/lshprung/gnu-make-dash-docset)|[link](http://www.gnu.org/software/make/)|[link](https://github.com/lshprung/gnu-make-dash-docset/releases/latest)|
|[ncurses](https://github.com/lshprung/ncurses-dash-docset)|[link](https://invisible-island.net/ncurses/)|[link](https://github.com/lshprung/ncurses-dash-docset/releases/latest)|

Library documentation is generated using doxygen. In the base of the repo, run

```
$ doxygen
```

HTML documentation will be generated under `docs/`

<!-- TODO:
  BUILD_FROM_SOURCE - compile the documentation from upstream, rather than downloading from a prebuild source (this is the default behavior for many docset generation scripts)

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
-->

<!--
|                                                      |LOCALE|NO_CSS|VERSION|
|------------------------------------------------------|------|------|-------|
|[debmake](https://salsa.debian.org/debian/debmake) ([latest docset release](https://github.com/lshprung/debmake-dash-docset/releases/latest))|✓ (see [here](./src/configs/debmake/README.md))||✓|
|[flex](https://github.com/westes/flex) ([latest docset release](https://github.com/lshprung/flex-dash-docset/releases/latest))|||✓|
|[glibc (GNU C Library)](https://www.gnu.org/software/libc/libc.html) ([latest docset release](https://github.com/lshprung/gnu-libc-dash-docset/releases/latest))|||✓|
|[GNU_Autoconf](https://www.gnu.org/software/autoconf/) ([latest docset release](https://github.com/lshprung/gnu-autoconf-dash-docset/releases/latest))|||✓|
|[GNU_Autoconf_Archive](https://www.gnu.org/software/autoconf-archive/) ([latest docset release](https://github.com/lshprung/gnu-autoconf-archive-dash-docset/releases/latest))|||✓|
|[GNU_Automake](https://www.gnu.org/software/automake/) ([latest docset release](https://github.com/lshprung/gnu-automake-dash-docset/releases/latest))||||
|[GNU_Bash](https://www.gnu.org/software/bash/) ([latest docset release](https://github.com/lshprung/gnu-bash-dash-docset/releases/latest))||||
|[GNU_Bison](https://www.gnu.org/software/bison/) ([latest docset release](https://github.com/lshprung/gnu-bison-dash-docset/releases/latest))||||
|[GNU_Coding_Standards](https://savannah.gnu.org/projects/gnustandards) ([latest docset release](https://github.com/lshprung/gnu-coding-standards-dash-docset/releases/latest))||||
|[GNU_Coreutils](https://www.gnu.org/software/coreutils) ([latest docset release](https://github.com/lshprung/gnu-coreutils-dash-docset/releases/latest))||||
|[GNU_Guix](https://guix.gnu.org/) ([latest docset release](https://github.com/lshprung/gnu-guix-dash-docset/releases/latest))|||✓|
|[GNU_Libtool](https://www.gnu.org/software/libtool/) ([latest docset release](https://github.com/lshprung/gnu-libtool-dash-docset/releases/latest))||||
|[GNU_Make](http://www.gnu.org/software/make/) ([latest docset release](https://github.com/lshprung/gnu-make-dash-docset/releases/latest))||✓||
|[ncurses](https://invisible-island.net/ncurses/) ([latest docset release](https://github.com/lshprung/ncurses-dash-docset/releases/latest))|||✓|

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

-->
