# Radio Button in Tkinter

#importing modules
from tkinter import *


root = Tk()
root.title("Radiobutton")

lbl = Label(root, text="Choose your gender", font=('Georgia', 35))
lbl.place(x=150,y=0)

def get_val():
    selected_gender = str(gender.get())
    labl1 = Label(text="Your gender is "+selected_gender, font=('Georgia', 30))
    labl1.place(x=200,y=200)

gender = StringVar()

radio_button1 = Radiobutton(root, text="male", variable=gender,value="male",font=("Aptos",20))
radio_button1.place(x=250,y=70)
gender.set("male")

radio_button2 = Radiobutton(root, text="female", variable=gender,value="female",font=("Aptos",20))
radio_button2.place(x=350,y=70)

btn1 = Button(root,text="Get gender",command=get_val, font=('Georgia', 25),background='red',foreground='green')
btn1.place(x=270,y=120)

root.mainloop()