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
    def __init__(self, type, index_entry_class, db_path, html_path):
        self.type = type
        self.index_entry_class = index_entry_class
        self.db_path = db_path
        self.html_path = html_path

    # Get each term from an index page and insert
    def insert_index_terms(self):
        soup = BeautifulSoup(open(self.html_path), 'html.parser')
        terms = soup.find_all(class_=self.index_entry_class)

        for term in terms:
            self.insert_term(term)

    def insert_term(self, term):
        name = term.a.get_text()
        name = name.replace('"', '""')
        name = name.replace('\n', '')

        page_path = term.a['href']
        #page_path = page_path.head(1)
        page_path = os.path.join(os.path.dirname(self.html_path), page_path)
        page_path = re.sub(r'^.*Contents.Resources.Documents.', r'', page_path)

        logging.debug("term is " + pformat(term))
        logging.debug("name is " + pformat(name))
        logging.debug("page_path is " + pformat(page_path))

        insert(self.db_path, name, self.type, page_path)

if __name__ == '__main__':
    type = sys.argv[1]
    index_entry_class = sys.argv[2]
    db_path = sys.argv[3]
    html_path = sys.argv[4]

    main = Index_terms(type, index_entry_class, db_path, html_path)

    create_table(db_path)
    main.insert_index_terms()
