# Form using Tkinter

# importing the modules
from tkinter import *

root = Tk()

root.geometry("500x400")
root.config(background="#13d444")
root.resizable(False,False)


def confirm():
    print("Your datas are as follows : ")
    print("Nama  = "+inp1.get())
    print("Age  = "+inp2.get())
    print("DOB = "+inp3.get())
    print("Gender = "+inp4.get())


heading = Label(root,text="Registration Form",bg="#13d444",fg="red",font=("times new roman",35))
heading.pack()

name = Label(root,text="Name",bg="#13d444",font=("times new roman",20))
name.place(x=50,y=80)
inp1 = Entry(root,font=("times new roman",20))
inp1.place(x=150,y=80)

age = Label(root,text="Age",bg="#13d444",font=("times new roman",20))
age.place(x=50,y=130)
inp2 = Entry(root,font=("times new roman",20))
inp2.place(x=150,y=130)

dob = Label(root,text="DOB",bg="#13d444",font=("times new roman",20))
dob.place(x=50,y=180)
inp3 = Entry(root,font=("times new roman",20))
inp3.place(x=150,y=180)

gender = Label(root,text="Gender",bg="#13d444",font=("times new roman",20))
gender.place(x=50,y=230)
inp4 = Entry(root,font=("times new roman",20))
inp4.place(x=150,y=230)


btn1 = Button(root,text="Submit",font=('times new roman',30),cursor="hand2",command=confirm)
btn1.place(x=180,y=300)

root.mainloop()