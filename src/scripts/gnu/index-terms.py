#!/usr/bin/env python3

from bs4 import BeautifulSoup
import logging
import sys

sys.path.append("..")

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
        name = term.get_text()
        name = name.replace('"', '""')
        name = name.replace('\n', '')

        page_path = term['href']
        #page_path = page_path.head(1)

        logging.debug("term is " + term)
        logging.debug("name is " + name)
        logging.debug("page_path is " + page_path)

        insert(self.db_path, name, self.type, page_path)

if __name__ == '__main__':
    main = Index_terms(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

    create_table(sys.argv[3])
    main.insert_index_terms()
