# Text varibale in tkinter

# importing tkinter modules
from tkinter import *



root = Tk()

def update_label():
    strvar.set("Hello " + entry.get())

name_label = Label(root, text="Enter your name:")
name_label.pack()

entry = Entry(root)
entry.pack()

# Use a StringVar to update the label text
strvar = StringVar()
lbl = Label(root, textvariable=strvar)
lbl.pack()

# Function to update the label when a button is clicked
update_button = Button(root, text="Update", command=update_label)
update_button.pack()

root.mainloop()
