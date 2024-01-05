#importing the modules
from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("300x200") 
  
w = Label(root, text ='GeeksForGeeks', font = "50")  
w.pack() 

messagebox.askquestion('Question','Are you sure?')

root.mainloop()