#!/usr/bin/env python3

from bs4 import BeautifulSoup, Tag
import logging
from pathlib import Path
from pprint import pformat
import re

from .create_table import create_table
from .insert import insert

class Gnu_Index_Terms:
    def __init__(self, 
                 type: str, 
                 db_path: str, 
                 html_path: str, 
                 index_entry_class: str | None = None
    ) -> None:
        self.type: str = type
        self.db_path: str = db_path
        self.html_path: str = html_path
        self.index_entry_class: str | None = index_entry_class

        create_table(db_path)
        self.insert_index_terms()

    def insert_index_terms(self) -> None:
        soup: BeautifulSoup = BeautifulSoup(
                open(self.html_path), 'html.parser'
        )
        terms: list[Tag] | filter[Tag]
        if self.index_entry_class:
            terms = soup.find_all(class_=self.index_entry_class)
        else:
            terms = soup.find_all("td")

        for term in terms:
            logging.debug("Checking term " + pformat(term))
            logging.debug("\tget_text() produces " + pformat(term.get_text()))

        if self.index_entry_class:
            terms = filter(
                lambda x: re.search(
                    r'.*:$', 
                    x.get_text().lstrip().rstrip()
                ), 
                terms)

        for term in terms:
            self.insert_term(term)

    def insert_term(self, term: Tag) -> None:
        name: str
        if term.a:
            name = term.a.get_text()
            name = name.replace('"', '""')
            name = name.replace('\n', '')
            name = name.lstrip()
            name = re.sub(r'\s{3,}', ' ', name)

            page_path: Path = Path(self.html_path).parent.joinpath(
                    str(term.a['href'])
            ).resolve()
            # remove part of path leading up to actual interest
            for i in range(len(page_path.parts)):
                if page_path.parts[i:i+2] == (
                        "Contents", "Resources", "Documents"
                ):
                    page_path = Path(*page_path.parts[i+3:])
                    break

            insert(self.db_path, name, self.type, str(page_path))
