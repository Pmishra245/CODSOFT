from tkinter import *

win = Tk()
win.config(bg='#34eb9b')
win.geometry ('800x600')
win.resizable(0,0)
win.title("Calculator")

label1 = Label(win,text="CALCULATOR",font=("Arial",40))
label1.config(fg='White',bg='#34eb9b')
label1.grid(row=0,columnspan=2,pady=30)

label2 = Label(win,text="Enter First Number:",font=("Arial",20))
label2.config(fg="Black",bg="#34eb9b")
label2.grid(row=1,column=0,pady=10,padx=10)

ent2 = Entry(win,font=("Arial",20))
ent2.grid(row=1,column=1,pady=10,padx=10)

label3 = Label(win,text="Enter Second Number:",font=("Arial",20))
label3.config(fg='Black',bg='#34eb9b')
label3.grid(row=2,column=0,pady=10,padx=10)

ent3 = Entry(win,font=("Arial",20))
ent3.grid(row=2,column=1,pady=10,padx=10)


add = Button(win,text="+",font=("Arial",20),bg='white')
add.grid(row=4,columnspan=1,padx=100,pady=10)

sub = Button(win,text="-",font=("Arial",20),bg='White')
sub.grid(row=4,columnspan=2,padx=10,pady=10)

mul = Button(win,text="x",font=("Arial",20),bg='white')
mul.grid(row=4,column=1,padx=70,pady=10)

div = Button(win,text="/",font=("Arial",20),bg='white')
div.grid(row=4,column=2,pady=10)

win.mainloop()