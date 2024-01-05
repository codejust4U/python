# Listbox in tkinter

# importing modules
from tkinter import *

root = Tk()

lbl1 = Label(root,text='Listbox',font=('castellar',35))
lbl1.pack()

list1 = ['C',
         'C++',
         'Python',
         'Java',
         'Typescript']

list_box1=Listbox(root,font=('georgia',25))
list_box1.pack()
for i in list1:
    list_box1.insert(END,i)


def list_btn():
    for i in list_box1.curselection():
        item=list_box1.get(i)
        lbl2 = Label(root,text=item,font=('georgia',25))
        lbl2.pack()



btn1 = Button(root,text='Get item from listbox',font=('Georgia',30),command=list_btn)
btn1.pack()

root.mainloop()