import tkinter as tk
from tkinter.font import Font

def button_functions (num):#this function Handles the function when the button clicked
    text = num.widget.cget("text")
    if text == "=":
        try:
            result = eval(operation_box.get())  
            operation_box.delete(0, tk.END)
            operation_box.insert(tk.END, str(result))
        except Exception as e:
            operation_box.delete(0, tk.END)
            operation_box.insert(tk.END, "Error")
    elif text == "C":
        back = operation_box.get()
        operation_box.delete(len(back)-1, tk.END)
    
    elif text == "AC":
        operation_box.delete(0, tk.END)

    else:
        operation_box.insert(tk.END, text)


win = tk.Tk()
win.title("Calculator")
win.geometry("400x500")
win.resizable(0,0)
win.config(bg="#c8e099")

operation_box = tk.Entry(win, state="normal", font=("typewriter",30),width=45,justify="right")
operation_box.grid(row = 0,column=0,columnspan=5,padx=100,pady=10)
operation_box.bind("<Key>", lambda e: "break")

operation_buttons = (
    "AC","**", "C", "/",
    "7","8", "9", "*",
    "4","5", "6", "-",
    "1","2", "3", "+",
    "00","0",".","="
)

c = 0  # column
r = 1  # row
button_index = 0

while button_index < len(operation_buttons):
    button_text = operation_buttons[button_index]
    btn = tk.Button(win, text=button_text, font=("typewriter",20),borderwidth=3 ,padx=10, pady=10, width=10, height=6, bg="#f7faf9")
    #grid helps to the buttons to place in their respective rows and columns
    btn.grid(row=r, column=c, padx=5, pady=5)
    c += 1
    if c > 3:
        c = 0
        r += 1
    button_index += 1

row_index = 1
while row_index < 6:
    win.grid_rowconfigure(row_index, weight=1)
    row_index += 1

column_index = 0
while column_index < 4:
    win.grid_columnconfigure(column_index, weight=1)
    column_index += 1

child_index = 0
while child_index < len(win.winfo_children()):
    btn = win.winfo_children()[child_index]
    btn.bind("<Button-1>", button_functions)
    child_index += 1

win.mainloop()
