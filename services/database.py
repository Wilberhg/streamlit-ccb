import sqlite3

database = "cafecombug.db"
cnxn = sqlite3.connect(database)
cursor = cnxn.cursor()