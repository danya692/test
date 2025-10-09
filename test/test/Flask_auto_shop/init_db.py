import sqlite3

coon = sqlite3.connect("database=db")

coon.execute()
coon.commit()
coon.close()
