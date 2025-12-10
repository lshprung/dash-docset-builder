import logging
from pathlib import Path
from pprint import pformat
import sqlite3

class DB:
    """! Docset database interface"""

    ## @var path
    #  path of the sqlite database

    def __init__(self, db_path: Path) -> None:
        """! Set member variables and create table

        @param db_path    path to the database file
        """
        
        self.path: Path = db_path
        self.create_table()
        
    def create_table(self) -> None:
        """! Create sqlite3 table at specified database file path

        The table will have the necessary constraints for a dash docset
        """

        con: sqlite3.Connection = sqlite3.connect(self.path)
        cur: sqlite3.Cursor = con.cursor()
        _ = cur.execute(
        """
        DROP TABLE IF EXISTS searchIndex
        """
        )
        _ = cur.execute(
        """
        CREATE TABLE IF NOT EXISTS searchIndex(id INTEGER PRIMARY KEY, name TEXT, 
        type TEXT, path TEXT);
        """
        )
        _ = cur.execute(
        """
        CREATE UNIQUE INDEX IF NOT EXISTS anchor ON searchIndex (name, type, path);
        """
        )
        con.close()

    def insert(self, name: str, type: str, page_path: str) -> None:
        """! Insert an index entry into the searchIndex table

        @param name         index entry name
        @param type         index entry type
        @param page_path    index entry page path
        """

        logging.debug("Inserting into " + str(self.path) + " with the following:")
        logging.debug("\tname = " + name)
        logging.debug("\ttype = " + type)
        logging.debug("\tpage_path = " + page_path)

        con = sqlite3.connect(self.path)
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
