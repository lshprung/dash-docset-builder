#!/usr/bin/env python3

import logging
import sqlite3
import sys

logging.basicConfig(level="DEBUG")

def insert(db_path, name, type, page_path):
    logging.debug("Inserting into " + db_path + " with the following:")
    logging.debug("\tname = " + name)
    logging.debug("\ttype = " + type)
    logging.debug("\tpage_path = " + page_path)

    con = sqlite3.connect(db_path)
    cur = con.cursor()
    query = "INSERT INTO searchIndex(name, type, path) VALUES (\"{name}\",\"{type}\",\"{page_path}\");".format(name = name, type = type, page_path = page_path)

    cur.execute(query)
    con.commit()
    con.close()

if __name__ == '__main__':
    insert(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
