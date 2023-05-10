import sqlite3 as lite


con = lite.connect('dados.db')

# Inserting Data (Create)


def insert_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO challenge (Tempo, Data, Contagem, log, Reducao) VALUES (?, ?, ?, ?, ?)"
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


# Updating Data (Update)


def update_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE challenge SET Tempo=?, Data=?, Contagem=?, log=?, Reducao=? WHERE id=?"
        cur.execute(query, i)


# Deleting Data (Delete)


def delete_info(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM challenge WHERE id=?"
        cur.execute(query, i)
