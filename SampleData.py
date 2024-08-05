import sqlite3
db = sqlite3.connect("pizza.db")
cursor = db.cursor()
with open("inserts.sql") as file:
    for line in file:
        cursor.execute(line.strip())

db.commit()
db.close()