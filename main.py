from tkinter import *
from tkcalendar import DateEntry


#---------- UI Setup ----------#

window = Tk()
window.title("Challenge Test")
window.geometry("1130x545")
window.resizable(width=False, height=False)

frame_title = Frame(window, width=1130, height=50, background="black", relief="flat")
frame_title.grid(row=0, column=0, columnspan=2)

frame_left = Frame(window, width=565, height=495, background="#feffff", relief="flat")
frame_left.grid(row=1, column=0, rowspan=2)

frame_right_top = Frame(window, width=565, height=248, background="green", relief="flat")
frame_right_top.grid(row=1, column=1)

frame_right_bottom = Frame(window, width=565, height=247, background="red", relief="flat")
frame_right_bottom.grid(row=2, column=1)

#---------- App Title ----------#

app_name = Label(frame_title, text="Challenge Test", font='Ivy 15 bold', 
	bg="black", fg="white", relief='flat')
app_name.place(x=483, y=11)


#---------- Periods ----------#

label_time = Label(frame_left, text='Tempo *', anchor=NW, font='Ivy 10 bold', 
	bg="#feffff", fg="#403d3d", relief='flat')
label_time.place(x=10, y=10)

entry_time0 = Entry(frame_left, width=10, justify='left', relief='solid')
entry_time0.place(x=15, y=30)
entry_time0.insert(0, "T0")

entry_time1 = Entry(frame_left, width=10, justify='left', relief='solid')
entry_time1.place(x=15, y=55)
entry_time1.insert(0, "T1")

entry_time2 = Entry(frame_left, width=10, justify='left', relief='solid')
entry_time2.place(x=15, y=80)
entry_time2.insert(0, "T2")

entry_time3 = Entry(frame_left, width=10, justify='left', relief='solid')
entry_time3.place(x=15, y=105)
entry_time3.insert(0, "T3")

entry_time4 = Entry(frame_left, width=10, justify='left', relief='solid')
entry_time4.place(x=15, y=130)
entry_time4.insert(0, "T7")

entry_time5 = Entry(frame_left, width=10, justify='left', relief='solid')
entry_time5.place(x=15, y=155)
entry_time5.insert(0, "T14")

entry_time6 = Entry(frame_left, width=10, justify='left', relief='solid')
entry_time6.place(x=15, y=180)
entry_time6.insert(0, "T21")

entry_time7 = Entry(frame_left, width=10, justify='left', relief='solid')
entry_time7.place(x=15, y=205)
entry_time7.insert(0, "T28")


#---------- Dates ----------#

label_date = Label(frame_left, text='Data *', anchor=NW, font='Ivy 10 bold', 
	bg="#feffff", fg="#403d3d", relief='flat')
label_date.place(x=80, y=10)

entry_date0 = DateEntry(frame_left, width=10, background='darkblue', foreground='white', borderwidth=2)
entry_date0.place(x=80, y=30)

entry_date1 = DateEntry(frame_left, width=10, background='darkblue', foreground='white', borderwidth=2)
entry_date1.place(x=80, y=55)

entry_date2 = DateEntry(frame_left, width=10, background='darkblue', foreground='white', borderwidth=2)
entry_date2.place(x=80, y=80)

entry_date3 = DateEntry(frame_left, width=10, background='darkblue', foreground='white', borderwidth=2)
entry_date3.place(x=80, y=105)

entry_date4 = DateEntry(frame_left, width=10, background='darkblue', foreground='white', borderwidth=2)
entry_date4.place(x=80, y=130)

entry_date5 = DateEntry(frame_left, width=10, background='darkblue', foreground='white', borderwidth=2)
entry_date5.place(x=80, y=155)

entry_date6 = DateEntry(frame_left, width=10, background='darkblue', foreground='white', borderwidth=2)
entry_date6.place(x=80, y=180)

entry_date7 = DateEntry(frame_left, width=10, background='darkblue', foreground='white', borderwidth=2)
entry_date7.place(x=80, y=205)

window.mainloop()