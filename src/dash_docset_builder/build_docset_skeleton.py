#!/usr/bin/env python3

import os
from pathlib import Path

def build_docset_skeleton(
        docset_name: str, 
        build_dir: Path | None = None
) -> dict[str, Path] | None:

    output: dict[str, Path] = {}

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
    output["docset_dir"] = build_dir.joinpath(f"{docset_name}.docset")
    output["contents_dir"] = output["docset_dir"].joinpath("Contents")
    output["resources_dir"] = output["contents_dir"].joinpath("Resources")
    output["documents_dir"] = output["resources_dir"].joinpath("Documents")
    output["documents_dir"].mkdir(parents = True, exist_ok = True)

    # create references to where files should go
    output["info_plist_file"] = output["contents_dir"].joinpath("Info.plist")
    output["index_file"] = output["resources_dir"].joinpath("docSet.dsidx")
    output["icon_file"] = output["docset_dir"].joinpath("icon.png")

    return output
