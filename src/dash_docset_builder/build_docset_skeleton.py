#!/usr/bin/env python3

import os
from pathlib import Path

def build_docset_skeleton(docset_name: str, build_dir: Path | None = None):
    # TODO determine default behavior if no build_dir is specified
    # for now, just make it the cwd
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
    docset_dir = build_dir.joinpath(f"{docset_name}.docset")
    contents_dir = docset_dir.joinpath("Contents")
    resources_dir = contents_dir.joinpath("Resources")
    documents_dir = resources_dir.joinpath("Documents")
    documents_dir.mkdir(parents = True, exist_ok = True)
