# Scrollbar in tkinter

#importing the modules
from tkinter import *
from tkinter import ttk

root = Tk()

root.geometry("150x200") 
lbl1 = Label(root,text='Scrollbar',font=('castellar',35))
lbl1.pack()

frame1 = Frame(root)
frame1.pack()

scroll_y = Scrollbar(root)
scroll_y.pack(side=RIGHT,fill=Y)

list1 = Listbox(root,yscrollcommand=scroll_y.set,font=('georgia',25))
for i in range(1,16):
    list1.insert(END,'Subject '+str(i))

list1.pack(side=LEFT,fill=BOTH)
scroll_y.config(command=list1.yview)


root.mainloop()