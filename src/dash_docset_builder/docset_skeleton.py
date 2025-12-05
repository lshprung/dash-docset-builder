#!/usr/bin/env python3

import os
from pathlib import Path

class DocsetSkeleton:
    """! Easy docset structure hierarchy reference

    Generates a docset filestructure hierarhcy and provides relevant path
    references.
    """

    ## @var docset_dir
    #  path of the docset dir (`docset_name`.docset)

    ## @var contents_dir
    #  path of the Contents dir (under docset_dir)

    ## @var resources_dir
    #  path of the Resources dir (under contents_dir)
    
    ## @var documents_dir
    #  path of the Documents dir (under resources_dir).

    ## @var info_plist_file
    #  path of the Info.plist file (under contents_dir)

    ## @var index_file
    #  path of the docSet.dsidx file (under resources_dir)

    ## @var icon_file
    #  path of the icon.png file (under docset_dir)

    def __init__(
            self, 
            docset_name: str, 
            build_dir: Path | None = None
    ) -> None:
        """! Class initializer

        @param docset_name    docset_name, for use in constructing docset_dir
        @param build_dir      build directory, as determined by the 
                              ArgumentParser
        """
        self.docset_dir: Path
        self.contents_dir: Path
        self.resources_dir: Path
        self.documents_dir: Path
        self.info_plist_file: Path
        self.index_file: Path
        self.icon_file: Path

        if build_dir is None:
            build_dir = Path('.')

        # ensure valid build_dir
        if not build_dir.is_dir():
            print(f"Error: '{str(build_dir)}' is not a directory")
            exit()
        if not os.access(build_dir, os.W_OK):
            print(f"Error: '{str(build_dir)}' is not writable")
            exit()

        # create the directories
        self.docset_dir = build_dir.joinpath(f"{docset_name}.docset")
        self.contents_dir = self.docset_dir.joinpath("Contents")
        self.resources_dir = self.contents_dir.joinpath("Resources")
        self.documents_dir = self.resources_dir.joinpath("Documents")
        self.documents_dir.mkdir(parents = True, exist_ok = True)

        # create references to where files should go
        self.info_plist_file = self.contents_dir.joinpath("Info.plist")
        self.index_file = self.resources_dir.joinpath("docSet.dsidx")
        self.icon_file = self.docset_dir.joinpath("icon.png")
