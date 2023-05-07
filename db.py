import sqlite3 as lite

con = lite.connect('dados.db')

with con:
	cur = con.cursor()
	cur.execute("CREATE TABLE challenge(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
		'Tempo (Dias)' TEXT, Data DATE, 'Contagem (UFC/mL)' INTEGER, 'log(UFC/mL)' REAL, '% Percentual de Redução' REAL)")