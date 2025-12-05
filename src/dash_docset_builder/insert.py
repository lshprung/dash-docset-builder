import logging
from pathlib import Path
from pprint import pformat
import sqlite3

def insert(db_path: Path, name: str, type: str, page_path: str) -> None:
    """! Insert an index entry into the sqlite table

    @param db_path      sqlite database file path
    @param name         index entry name
    @param type         index entry type
    @param page_path    index entry page path
    """
    logging.debug("Inserting into " + str(db_path) + " with the following:")
    logging.debug("\tname = " + name)
    logging.debug("\ttype = " + type)
    logging.debug("\tpage_path = " + page_path)

    con = sqlite3.connect(db_path)
    cur = con.cursor()
    query = f"""
    INSERT INTO searchIndex(name, type, path) VALUES (\"{name}\",\"{type}\",
    \"{page_path}\");
    """

    try:
        _ = cur.execute(query)
        con.commit()
    except sqlite3.IntegrityError as e:
        logging.warning("Skipping query: " + pformat(e))
    con.close()
