import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO blocks (header, hash) VALUES (?, ?)",
            (' ', 'Welcome to SleekBlog')
            )

connection.commit()
connection.close()
