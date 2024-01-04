# Combobox in Tkinter

#importing the modules

from tkinter import *
from tkinter import ttk

root = Tk()

lbl1 = Label(root,text="Combobox",font=('Castellar',35,'bold'),foreground='red')
lbl1.pack(pady=20)

lbl2 = Label(root,text='Choose your subject',font=('times new roman',20))
lbl2.pack()

combo_box1 = ttk.Combobox(root,font=('times new roman',15),width=30)
combo_box1['values'] = ('Web Technology',
                        'Software engineering',
                        'Computer networks',
                        'Object Oriented Programming',
                        'Big Data')
combo_box1.set('Web Technology')
combo_box1.pack()

def get_subject():
    selected_subject = combo_box1.get()
    lbl3 = Label(root,text="You choosed "+selected_subject,font=('times new roman',15))
    lbl3.pack()


btn1 = Button(root,text="Get your subject",font=('times new roman',15),command=get_subject)
btn1.pack(pady=10)

root.mainloop()