from tkinter import *


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


app_name = Label(frame_title, text="Challenge Test", font='Ivy 15 bold', 
	bg="black", fg="white", relief='flat')
app_name.place(x=483, y=11)

label_time = Label(frame_left, text='Tempo *', anchor=NW, font='Ivy 10 bold', 
	bg="#feffff", fg="#403d3d", relief='flat')
label_time.place(x=10, y=10)

entry_time0 = Entry(frame_left, width=15, justify='left', relief='solid')
entry_time0.place(x=15, y=30)
entry_time0.insert(0, "T0")


window.mainloop()