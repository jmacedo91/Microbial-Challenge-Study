from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
import numpy as np

from view import *


# ---------- UI Setup ---------- #

window = Tk()
window.title("Challenge Test - PróLab Biotecnologia")
window.geometry("1130x600")
window.resizable(width=False, height=False)
global tree

# ---------- Frames ---------- #

frame_title = Frame(window, width=1130, height=100, background="#01304E", relief="flat")
frame_title.grid(row=0, column=0, columnspan=2)

frame_left = Frame(window, width=465, height=500, background="#01304E", relief="flat")
frame_left.grid(row=1, column=0, rowspan=2)

prolab_canvas = Canvas(width=300, height=100, highlightthickness=0, background="#01304E")
prolab_img = PhotoImage(file="images/prolablogo.png")
prolab_canvas.create_image(150, 50, image=prolab_img)
prolab_canvas.place(x=15, y=0)

frame_right_top = Frame(window, width=665, height=250, relief="flat")
frame_right_top.grid(row=1, column=1)

frame_right_bottom = Frame(window, width=665, height=250, background="red", relief="flat")
frame_right_bottom.grid(row=2, column=1)

# ---------- App Title ---------- #

app_name = Label(frame_title, text="Challenge Test", font='Ivy 30 bold', bg="#01304E", fg="white", relief='flat')
app_name.place(x=450, y=25)

# ---------- Relatory Number ---------- #

label_rel_number = Label(frame_left, text="Relatório de Ensaio nº: ", anchor=NW, font='Ivy 10 bold',
                         bg="#01304E", fg="white", relief="flat")
label_rel_number.place(x=15, y=10)

entry_rel_number = Entry(frame_left, width=41, justify="left", relief="solid", bd=2)
entry_rel_number.place(x=168, y=10)
entry_rel_number.focus()

# ---------- Initial Count ---------- #

initial_count = Label(frame_left, text="Contagem Inicial: ", anchor=NW, font='Ivy 10 bold',
                         bg="#01304E", fg="white", relief="flat")
initial_count.place(x=15, y=35)

initial_count_entry = Entry(frame_left, width=41, justify="left", relief="solid", bd=2)
initial_count_entry.place(x=168, y=35)

# ---------- Periods ---------- #


label_time = Label(frame_left, text='Tempo (Dias):', anchor=NW, font='Ivy 10 bold', bg="#01304E", fg="white",
                   relief='flat')
label_time.place(x=15, y=60)

entry_time0 = Entry(frame_left, width=20, justify='center', relief='solid', bd=2)
entry_time0.place(x=15, y=85)
entry_time0.insert(0, "T0")

entry_time1 = Entry(frame_left, width=20, justify='center', relief='solid', bd=2)
entry_time1.place(x=15, y=110)
entry_time1.insert(0, "T1")

entry_time2 = Entry(frame_left, width=20, justify='center', relief='solid', bd=2)
entry_time2.place(x=15, y=135)
entry_time2.insert(0, "T2")

entry_time3 = Entry(frame_left, width=20, justify='center', relief='solid', bd=2)
entry_time3.place(x=15, y=160)
entry_time3.insert(0, "T3")

entry_time4 = Entry(frame_left, width=20, justify='center', relief='solid', bd=2)
entry_time4.place(x=15, y=185)
entry_time4.insert(0, "T7")

entry_time5 = Entry(frame_left, width=20, justify='center', relief='solid', bd=2)
entry_time5.place(x=15, y=210)
entry_time5.insert(0, "T14")

entry_time6 = Entry(frame_left, width=20, justify='center', relief='solid', bd=2)
entry_time6.place(x=15, y=235)
entry_time6.insert(0, "T21")

entry_time7 = Entry(frame_left, width=20, justify='center', relief='solid', bd=2)
entry_time7.place(x=15, y=260)
entry_time7.insert(0, "T28")

entry_time = [entry_time0, entry_time1, entry_time2, entry_time3, entry_time4, entry_time5, entry_time6, entry_time7]

# ---------- Dates ---------- #

label_date = Label(frame_left, text='Data:', anchor=NW, font='Ivy 10 bold', bg="#01304E", fg="white", relief='flat')
label_date.place(x=145, y=60)

entry_date0 = DateEntry(frame_left, date_pattern='dd/mm/yyyy', width=20, background='darkblue', foreground='white',
                        borderwidth=2)
entry_date0.delete(0, 'end')
entry_date0.place(x=145, y=85)

entry_date1 = DateEntry(frame_left, date_pattern='dd/mm/yyyy', width=20, background='darkblue', foreground='white',
                        borderwidth=2)
entry_date1.delete(0, 'end')
entry_date1.place(x=145, y=110)

entry_date2 = DateEntry(frame_left, date_pattern='dd/mm/yyyy', width=20, background='darkblue', foreground='white',
                        borderwidth=2)
entry_date2.delete(0, 'end')
entry_date2.place(x=145, y=135)

entry_date3 = DateEntry(frame_left, date_pattern='dd/mm/yyyy', width=20, background='darkblue', foreground='white',
                        borderwidth=2)
entry_date3.delete(0, 'end')
entry_date3.place(x=145, y=160)

entry_date4 = DateEntry(frame_left, date_pattern='dd/mm/yyyy', width=20, background='darkblue', foreground='white',
                        borderwidth=2)
entry_date4.delete(0, 'end')
entry_date4.place(x=145, y=185)

entry_date5 = DateEntry(frame_left, date_pattern='dd/mm/yyyy', width=20, background='darkblue', foreground='white',
                        borderwidth=2)
entry_date5.delete(0, 'end')
entry_date5.place(x=145, y=210)

entry_date6 = DateEntry(frame_left, date_pattern='dd/mm/yyyy', width=20, background='darkblue', foreground='white',
                        borderwidth=2)
entry_date6.delete(0, 'end')
entry_date6.place(x=145, y=235)

entry_date7 = DateEntry(frame_left, date_pattern='dd/mm/yyyy', width=20, background='darkblue', foreground='white',
                        borderwidth=2)
entry_date7.delete(0, 'end')
entry_date7.place(x=145, y=260)

entry_date = [entry_date0, entry_date1, entry_date2, entry_date3, entry_date4, entry_date5, entry_date6, entry_date7]

# ---------- Counts ---------- #

label_count = Label(frame_left, text='Contagem:', anchor=NW, font='Ivy 10 bold', bg="#01304E", fg="white",
                   relief='flat')
label_count.place(x=294, y=60)

entry_count0 = Entry(frame_left, width=20, justify='left', relief='solid', bd=2)
entry_count0.place(x=294, y=85)

entry_count1 = Entry(frame_left, width=20, justify='left', relief='solid', bd=2)
entry_count1.place(x=294, y=110)

entry_count2 = Entry(frame_left, width=20, justify='left', relief='solid', bd=2)
entry_count2.place(x=294, y=135)

entry_count3 = Entry(frame_left, width=20, justify='left', relief='solid', bd=2)
entry_count3.place(x=294, y=160)

entry_count4 = Entry(frame_left, width=20, justify='left', relief='solid', bd=2)
entry_count4.place(x=294, y=185)

entry_count5 = Entry(frame_left, width=20, justify='left', relief='solid', bd=2)
entry_count5.place(x=294, y=210)

entry_count6 = Entry(frame_left, width=20, justify='left', relief='solid', bd=2)
entry_count6.place(x=294, y=235)

entry_count7 = Entry(frame_left, width=20, justify='left', relief='solid', bd=2)
entry_count7.place(x=294, y=260)

entry_count = [entry_count0, entry_count1, entry_count2, entry_count3, entry_count4, entry_count5, entry_count6,
               entry_count7]

# ---------- Frame Direita ---------- #


def show_table():

    global tree

    my_list = show_info()

    table_header = ['ID', 'Tempo (Dias)', 'Data', 'Contagem (UFC/mL)', 'log(UFC/mL)', '% Percentual de Redução']

    tree = ttk.Treeview(frame_right_top, selectmode='extended', columns=table_header, show='headings')

    # Vertical Scroll Bar
    vsb = ttk.Scrollbar(frame_right_top, orient='vertical', command=tree.yview)

    # Horizontal Scroll Bar
    hsb = ttk.Scrollbar(frame_right_top, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_right_top.grid_rowconfigure(0, weight=12)

    hd = ['center', 'center', 'center', 'center', 'center', 'center']
    h = [40, 100, 90, 133, 113, 166]
    n = 0

    for col in table_header:
        tree.heading(col, text=col, anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    for item in my_list:
        tree.insert('', 'end', values=item)


def insert():
    for row in range(8):
        if entry_count[row].get() != '' and entry_date[row].get() != '':
            tempo = entry_time[row].get()
            data = entry_date[row].get()
            try:
                contagem = float(entry_count[row].get().replace(",", "."))
                log_ufc = round(np.log10(contagem), 2)
                if initial_count_entry.get() == '':
                    messagebox.showerror("Erro de Cálculo.",
                                         "Insira a contagem inicial para o cálculo do percentual de redução.")
                else:
                    if tempo == 'T0':
                        reduction = '-'
                    else:
                        reduction = 100 * (1 - (1 / (
                                    10 ** (np.log10(float(initial_count_entry.get().replace(",", ".")) / contagem)))))
                        reduction = round(reduction, 2)

                    my_list = [tempo, data, contagem, log_ufc, reduction]

                    insert_info(my_list)

                    for widget in frame_right_top.winfo_children():
                        widget.destroy()

                show_table()
            except ValueError:
                messagebox.showerror("Erro!", 'Insira um número no campo "Contagem"')

    for row in range(8):
        entry_date[row].delete(0, 'end')
        entry_count[row].delete(0, 'end')


def update():
    try:
        treev_data = tree.focus()
        treev_dictionary = tree.item(treev_data)
        tree_list = treev_dictionary['values']

        id_value = tree_list[0]

        label_time_update = Label(frame_left, text='Tempo Correção', anchor=NW, font='Ivy 10 bold', bg="#01304E",
                                  fg="white", relief='flat')
        label_time_update.place(x=15, y=325)

        entry_time_update = Entry(frame_left, width=20, justify='center', relief='solid', bd=2)
        entry_time_update.place(x=15, y=345)
        entry_time_update.insert(0, tree_list[1])

        label_date_update = Label(frame_left, text='Data Correção', anchor=NW, font='Ivy 10 bold', bg="#01304E",
                                  fg="white", relief='flat')
        label_date_update.place(x=145, y=325)

        entry_date_update = DateEntry(frame_left, date_pattern='dd/mm/yyyy', width=20, background='darkblue',
                                      foreground='white', borderwidth=2)
        entry_date_update.place(x=145, y=345)
        entry_date_update.delete(0, 'end')
        entry_date_update.insert(0, tree_list[2])

        label_count_update = Label(frame_left, text='Contagem Correção', anchor=NW, font='Ivy 10 bold', bg="#01304E",
                                   fg="white", relief='flat')
        label_count_update.place(x=294, y=325)

        entry_count_update = Entry(frame_left, width=20, justify='center', relief='solid', bd=2)
        entry_count_update.place(x=294, y=345)
        entry_count_update.insert(0, tree_list[3])

        def update():
            time = entry_time_update.get()
            date = entry_date_update.get()
            count = float(entry_count_update.get().replace(",", "."))
            log_ufc = round(np.log10(count), 2)

            if initial_count_entry.get() == '':
                messagebox.showerror("Erro de Cálculo.",
                                     "Insira a contagem inicial para atualizar o percentual de redução.")
            else:
                if time == 'T0':
                    reduction = '-'
                else:
                    reduction = 100 * (1 - (1 / (10 ** (np.log10(float(initial_count_entry.get().replace(",", ".")) / count)))))
                    reduction = round(reduction, 2)
                update_list = [time, date, count, log_ufc, reduction, id_value]
                update_info(update_list)
                messagebox.showinfo("Sucesso!", "Dados Atualizados com Sucesso!")

            for widget in frame_right_top.winfo_children():
                widget.destroy()

            confirm_button.place_forget()
            label_time_update.place_forget()
            entry_time_update.place_forget()
            label_date_update.place_forget()
            entry_date_update.place_forget()
            label_count_update.place_forget()
            entry_count_update.place_forget()

            show_table()

        confirm_button = Button(frame_left, text="Confirmar", width=56, font='Ivy 9 bold', bg="#A0D8B3", fg="black",
                                relief="raised", overrelief="ridge", command=update)
        confirm_button.place(x=15, y=375)

    except IndexError:
        messagebox.showerror('Erro!', 'Selecionar um dos dados na tabela')


def delete():
    try:
        treev_data = tree.selection()
        tree_list = []
        id_list = []
        for row in treev_data:
            treev_dictionary = tree.item(row)
            tree_list.append(treev_dictionary['values'])

        for value in range(len(tree_list)):
            id_list.append(tree_list[value][0])

        for id_value in id_list:
            delete_info([id_value])

        messagebox.showinfo('Sucesso!', 'Dados deletados com sucesso!')

        for widget in frame_right_top.winfo_children():
            widget.destroy()

        show_table()

    except IndexError:
        messagebox.showerror('Erro!', 'Selecione um ou mais dados na tabela')


# ---------- Buttons ---------- #


insert_button = Button(frame_left, text="Inserir Dados", width=16, font="Ivy 9 bold", bg="#6fbbd3", fg="black",
                       relief='raised', overrelief='ridge', command=insert)
insert_button.place(x=15, y=290)

update_button = Button(frame_left, text="Atualizar", width=19, font='Ivy 9 bold', bg="#A0D8B3", fg="black",
                       relief='raised', overrelief='ridge', command=update)
update_button.place(x=145, y=290)

delete_button = Button(frame_left, text="Deletar", width=16, font='Ivy 9 bold', bg="#ff6961", fg="black",
                       relief='raised', overrelief='ridge', command=delete)
delete_button.place(x=294, y=290)

# Calling show_table function
show_table()

window.bind("<Control-d>", lambda event: delete())
window.mainloop()
