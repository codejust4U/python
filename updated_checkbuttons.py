# Ckeck buttons in tkinter

from tkinter import *
root = Tk()

lbl1 = Label(root, text="Choose your optional subjects", foreground="yellow", background="black", font=("Algerian", 35))
lbl1.place(x=200, y=50)

def confirm():
    opt_subs = [var.get() for var in check_vars]
    subjects = ", ".join(opt_subs)
    lbl2 = Label(root, text="Your optional subjects are: " + subjects, font=('Georgia', 30))
    lbl2.place(x=100, y=650)

check_vars = []

def create_checkbox(text, y_pos):
    var = StringVar()
    check_var = Checkbutton(root, text=text, variable=var, font=("Algerian", 25))
    check_var.place(x=150, y=y_pos)
    var.set("Off")
    check_vars.append(var)

create_checkbox("C", 150)
create_checkbox("C++", 200)
create_checkbox("Java", 250)
create_checkbox(".Net", 300)
create_checkbox("JS", 350)
create_checkbox("Python", 400)

btn1 = Button(root, text="Confirm", command=confirm, font=('Georgia', 30))
btn1.place(x=200, y=500)

root.mainloop()