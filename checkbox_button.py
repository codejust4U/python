# Check button in tkinter

# importing the modules
from tkinter import *

# importing the modules
from tkinter import *
root = Tk()

lbl1 = Label(root,text="Choose your optional subjects",foreground="yellow",background="black",font=("Algerian",35))
lbl1.place(x=200,y=50)

def confirm():
    opt_sub = str(check_var.get())
    lbl2 = Label(text="Your optional subjects are : "+opt_sub,font=('Georgia',30))
    lbl2.place(x=100,y=650)

check_var = StringVar()

check_box1 = Checkbutton(root,text="C",variable=check_var,font=("Algerian",25))
check_box1.place(x=150,y=150)
check_var.set("C")
check_box2 = Checkbutton(root,text="C++",variable=check_var,font=("Algerian",25))
check_box2.place(x=150,y=200)
check_var.set("C")
check_box3 = Checkbutton(root,text="Java",variable=check_var,font=("Algerian",25))
check_box3.place(x=150,y=250)
check_var.set("C")
check_box4 = Checkbutton(root,text=".Net",variable=check_var,font=("Algerian",25))
check_box4.place(x=150,y=300)
check_var.set("C")
check_box5 = Checkbutton(root,text="JS",variable=check_var,font=("Algerian",25))
check_box5.place(x=150,y=350)
check_var.set("C")
check_box6 = Checkbutton(root,text="Python",variable=check_var,font=("Algerian",25))
check_box6.place(x=150,y=400)
check_var.set("C")
btn1 = Button(root,text="Confirm",command=confirm,font=('Georgia',30))
btn1.place(x=200,y=500)
check_var.set("C")



root.mainloop()