import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

def view_stats():
    done_count = 0
    total_count = task_area.size()
    for i in range(total_count):
        if task_area.itemcget(i, "fg") == "green":
            done_count += 1
    messagebox.showinfo("Task Statistics", f"Total tasks: {total_count}\nCompleted tasks: {done_count}")

def add_task():
    task = task_add.get()
    if task != "":
        task_area.insert(tk.END, task)
        task_area.itemconfig(tk.END, fg="#75480d")
        task_add.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a task.")

def mark_done():
    task_index = task_area.curselection()
    if task_index:
        task_area.itemconfig(task_index, fg="green")
            
def delete_task():
    task_index = task_area.curselection()
    if task_index:
        task_area.delete(task_index)

def delete_all():
    task_area.delete(0, tk.END)        

# Create the main window

win = tk.Tk()
win.title("To-Do List")
win.config(bg ="#d6a75c")
win.geometry("600x500")
win.resizable(0,0)

#Creating Labels, Buttons and Entry boxes

lbl1 = Label(win, text="To-Do List", font=("Arial",25,"bold"))
lbl1.config(fg="#75480d",bg="#f5dba4")
lbl1.grid(row = 0,columnspan=3,padx=150 ,pady=10)

lbl2 = Label(win, text="Enter task here :", font=("Arial",20,"italic"))
lbl2.config(bg="#d6a75c",fg="#ffffff")
lbl2.grid(row = 2,padx= 10,pady=10)


task_add = Entry(win, font=("Arial",20))
task_add.config(justify="center",fg="#75480d")
task_add.grid(row = 2,column=1,padx= 10,pady=10)

submit_add = Button(win,text="Submit", font=("Arial",10,"bold"), command=add_task ,anchor="center", 
                    fg="#75480d",bg="#e8e19e",width=10, height=2)
submit_add.grid(row =3,columnspan =3,pady=10)

task_area = Listbox(win,height=10,width=30,font=("Arial",15),borderwidth=2)
task_area.grid(row=4,column = 1,rowspan=9,sticky='E')

done_button = Button(win,text="Done", font=("Arial",10,"bold"), command=mark_done , anchor="center",
                     fg="#75480d",bg="#e8e19e",width=20,height=2)
done_button.grid(row=5,column=0,padx=10,sticky='W')

stats_button = Button(win,text="View stats", font=("Arial",10,"bold"), command=view_stats ,anchor="center",
                      fg="#75480d",bg="#e8e19e",width=20,height=2)
stats_button.grid(row=7,column=0,padx=10,sticky='W')

delete_button = Button(win,text="Delete", font=("Arial",10,"bold"), command=delete_task , anchor="center",
                       fg="#75480d",bg="#e8e19e",width=20,height=2)
delete_button.grid(row=9,column=0,padx=10,sticky='W')

delete_all_button = Button(win,text="Delete All", font=("Arial",10,"bold"), command=delete_all, anchor="center",
                           fg="#75480d",bg="#e8e19e",width=20,height=2)
delete_all_button.grid(row=11,column=0,padx=10,sticky='W')


win.mainloop()