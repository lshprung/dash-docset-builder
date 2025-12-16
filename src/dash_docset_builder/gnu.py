#!/usr/bin/env python3

from bs4 import BeautifulSoup, Tag
import logging
from pathlib import Path
from pprint import pformat
import re

from .db import DB

class Gnu_Index_Terms:
    """! Class to handle indexing index entries from GNU documentation"""
    def __init__(self, 
                 type: str, 
                 db: DB, 
                 html_path: Path, 
                 index_entry_class: str | None = None
    ) -> None:
        """! Initializer

        @param type                 index type (see possible options here 
                                    https://kapeli.com/docsets#supportedentrytypes)
        @param db                   sqlite database for the docset
        @param html_path            index file html path
        @param index_entry_class    optionally look for a html class name that 
                                    index entries belong to

        This class does everything in the constructor. If index_entry_class is
        not included, then a colon (':') will be searched for instead to 
        determine what on the page is an entry to index.
        """
        self.type: str = type
        self.db: DB = db
        self.html_path: Path = html_path
        self.index_entry_class: str | None = index_entry_class

        self.insert_index_terms()

    def insert_index_terms(self) -> None:
        """! Determine the list of terms from the index and insert each one"""

        soup: BeautifulSoup = BeautifulSoup(
                open(self.html_path), 'html.parser'
        )
        terms: list[Tag]
        if self.index_entry_class:
            terms = soup.find_all(class_=self.index_entry_class)
        else:
            terms = soup.find_all("td")

        for term in terms:
            logging.debug("Checking term " + pformat(term))
            logging.debug("\tget_text() produces " + pformat(term.get_text()))

        # try to insert via looking for colon if no class to look for is 
        # provided
        if self.index_entry_class is None:
            for term in filter(
                    lambda x: re.search(
                        r'.*:$', x.get_text().lstrip().rstrip()
                    ), 
                    terms
            ):
                self.insert_term(term)
            return

        for term in terms:
            self.insert_term(term)

    def insert_term(self, term: Tag) -> None:
        """! Cleanup the name and link, and insert

        @param term    html tag of the term to insert
        """
        name: str
        if term.a:
            name = term.a.get_text()
            name = name.replace('"', '""')
            name = name.replace('\n', '')
            name = name.lstrip()
            name = re.sub(r'\s{3,}', ' ', name)

            page_path: Path = self.html_path.parent.joinpath(
                    str(term.a['href'])
            ).resolve()
            # remove part of path leading up to actual interest
            for i in range(len(page_path.parts)):
                if page_path.parts[i:i+3] == (
                        "Contents", "Resources", "Documents"
                ):
                    page_path = Path(*page_path.parts[i+3:])
                    break

            self.db.insert(name, self.type, str(page_path))
            return
