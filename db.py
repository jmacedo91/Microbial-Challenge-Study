import sqlite3 as lite

con = lite.connect('dados.db')

with con:
	cur = con.cursor()
	cur.execute("CREATE TABLE challenge(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
		Tempo TEXT, Data DATE, Contagem INTEGER, log REAL, Reducao REAL)")