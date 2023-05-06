import sqlite3 as lite

con = lite.connect('dados.db')

with con:
	cur = con.cursor()
	cur.execute("CREATE TABLE challenge(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
		Tempo TEXT, Data DATE, 'UFC/mL' INTEGER, 'log(UFC/mL)' REAL, '%PR' REAL)")