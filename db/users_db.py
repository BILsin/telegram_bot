import sqlite3


conn = sqlite3.connect('users.db')
cur = conn.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS users(
            user_id INT PRIMARY KEY,
            user_name TEXT );
""")
conn.commit()


def musicdb_add(user_id: int, user_name: str):
    cur.execute('INSERT INTO music(?, ?); VALUES (?, ?)')
    conn.commit()