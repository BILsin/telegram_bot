import sqlite3


conn = sqlite3.connect('musicbase.db')
cur = conn.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS music(
            musicid INT PRIMARY KEY,
            musicname TEXT,
            musichash TEXT );
""")
conn.commit()


def musicdb_add(musicid: int, musicname: str, musichash: str):
    cur.execute('INSERT INTO music(?, ?, ?); VALUES (?, ?, ?)')
    conn.commit()