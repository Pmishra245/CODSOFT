from tkinter import *
from tkinter import messagebox
import pyperclip
import random


def low():
	output.delete(0, END)

	length = var1.get()

	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	digits = "0123456789!@#$%^&*()ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
	password = ""

	if var.get() == 1:
		for i in range(0, length):
			password = password + random.choice(lower)
		return password

	elif var.get() == 2:
		for i in range(0, length):
			password = password + random.choice(upper)
		return password

	elif var.get() == 3:
		for i in range(0, length):
			password = password + random.choice(digits) 
		return password
	else:
		messagebox.showerror("Error","Please select the strength of your password")


def generate():
	password1 = low()
	output.insert(20, password1)


def copy():
	random_password = output.get()
	pyperclip.copy(random_password)


win = Tk()
var = IntVar()
var1 = IntVar()

win.title ("Password Generator")
win.geometry('500x320')
win.resizable(0,0)
win.config(bg='#a8bf80')

lbl1 = Label(win, text="Password Generator",font=("Arial",30,"italic"),)
lbl1.config(justify="center",fg="#86a158", bg="#fcfafc")
lbl1.grid(row = 0,padx = 70,pady=10)

lbl2 = Label(win,text="Password Length - ",font=("Arial",12,"bold"),background='#a8bf80',fg="white")
lbl2.grid(row = 1,padx = 10,sticky='W') 

output = Entry(win,border='5',justify="center",font=("typewriter",20))
output.grid(row = 2,padx = 60,pady = 10)
output.bind("<Key>", lambda e: "break")

copy_button = Button(win, text="Copy", command=copy)
copy_button.grid(row=5, padx = 20,pady=10)
generate_button = Button(win, text="Generate", command=generate)
generate_button.grid(row=4, padx = 40,pady=10)

low_level = Radiobutton(win, text="Low", variable=var, value=1)
low_level.grid(row=3, padx=100, sticky='E')
middle_level = Radiobutton(win, text="Medium", variable=var, value=2)
middle_level.grid(row=4, padx = 100, sticky='E')
strong_level = Radiobutton(win, text="Strong", variable=var, value=3)
strong_level.grid(row=5, padx = 100, sticky='E')

length_scale = Scale(win,width=20,length=170, bg = "white" ,from_=4, to_= 20,orient=HORIZONTAL,variable=var1)
length_scale.grid(row=1, padx = 70)

win.mainloop()