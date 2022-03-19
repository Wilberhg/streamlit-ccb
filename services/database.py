import sqlite3

database = "cafecombug.db"
cnxn = sqlite3.connect(database, check_same_thread=False)
cursor = cnxn.cursor()