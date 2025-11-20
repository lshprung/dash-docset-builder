import logging
from pprint import pformat
import sqlite3

logging.basicConfig(level="DEBUG")

def insert(db_path: str, name: str, type: str, page_path: str) -> None:
    logging.debug("Inserting into " + db_path + " with the following:")
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
