#!/usr/bin/env python3

from bs4 import BeautifulSoup
import logging
import os
from pprint import pformat
import re
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from create_table import create_table
from insert import insert

class Index_terms:
    def __init__(self, type, db_path, html_path):
        self.type = type
        self.db_path = db_path
        self.html_path = html_path

    def insert_index_terms(self):
        soup = BeautifulSoup(open(self.html_path), 'html.parser')
        terms = soup.find_all("td")

        for term in terms:
            logging.debug("Checking term " + pformat(term))
            logging.debug("\tget_text() produces " + pformat(term.get_text()))
        for term in filter(lambda x: re.search(r'.*:$', x.get_text()), terms):
            self.insert_term(term)

    def insert_term(self, term):
        name = term.a.get_text()
        name = name.replace('"', '""')
        name = name.replace('\n', '')

        page_path = term.a['href']

        insert(self.db_path, name, self.type, page_path)


if __name__ == '__main__':
    type = sys.argv[1]
    db_path = sys.argv[2]
    html_path = sys.argv[3]

    create_table(db_path)
    main = Index_terms(type, db_path, html_path)

    main.insert_index_terms()
