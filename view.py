import sqlite3 as lite


con = lite.connect('dados.db')

# Inserting Data (Create)


def insert_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO challenge ('Tempo (Dias)', Data, 'Contagem (UFC/mL)', 'log(UFC/mL)', \
        '% Percentual de Redução') VALUES (?, ?, ?, ?, ?)"
        cur.execute(query, i)


# Reading Data (Read)


def show_info():
    my_list = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM challenge"
        cur.execute(query)
        information = cur.fetchall()

        for i in information:
            my_list.append(i)
    return my_list


# Deleting Data (Delete)


def delete_info(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM challenge WHERE id=(?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)
