import sqlite3

# create sqlite database for searchIndex
def create_table(db_path: str) -> None:
    con = sqlite3.connect(db_path)
    cur = con.cursor()
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
