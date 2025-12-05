from pathlib import Path
import sqlite3

# create sqlite database for searchIndex
def create_table(db_path: Path) -> None:
    """! Create sqlite3 table at specified database file path

    @param db_path    path to the database file

    The table will have the necessary constraints for a dash docset
    """

    con = sqlite3.connect(db_path)
    cur = con.cursor()
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
