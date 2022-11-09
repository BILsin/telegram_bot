import sqlite3


conn = sqlite3.connect('musicbase.db')
cur = conn.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS music(
            musicid INT PRIMARY KEY,
            musichash TEXT,
            moderation TEXT,
            leadervote TEXT );
""")
conn.commit()


def musicdb_add(musicid: int, musichash: str, moderation: str, leadervote: str):
    cur.execute('INSERT INTO music(?, ?, ?, ?); VALUES (?, ?, ?, ?)')
    conn.commit()