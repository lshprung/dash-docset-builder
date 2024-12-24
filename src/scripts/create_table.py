#!/usr/bin/env python3

import sqlite3
import sys

# create sqlite database for searchIndex
def create_table(db_path):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);")
    cur.execute("CREATE UNIQUE INDEX IF NOT EXISTS anchor ON searchIndex (name, type, path);")
    con.close()

if __name__ == '__main__':
    create_table(sys.argv[1])
