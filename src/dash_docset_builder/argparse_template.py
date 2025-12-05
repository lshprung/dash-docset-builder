import argparse
from pathlib import Path

def get_argparse_template() -> argparse.ArgumentParser:
    """! generate base ArgumentParser object
    
    Takes a MANUAL_SOURCE argument and optional builddir.
    Add more arguments on top of the return object as you see fit

    """

    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    _ = parser.add_argument("MANUAL_SOURCE", type=Path,
                            help="Path to the manual source")
    _ = parser.add_argument("-b", "--builddir", default=".", type=Path,
                            help="Directory to build the docset in")
    return parser
