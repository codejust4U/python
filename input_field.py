# Taking input using input field
from tkinter import *

root = Tk()

inp1 = Entry(root)
inp1.pack()

def fact():
    try:
        n = int(inp1.get())  
        result = 1
        for i in range(1, n + 1):  #
            result *= i 
        lbl = Label(root, text="Factorial of " + str(n) + " is " + str(result))
        lbl.pack()
    except ValueError:
        lbl = Label(root, text="Please enter a valid number!")
        lbl.pack()

btn1 = Button(root, text="get factorial", command=fact)
btn1.pack()

root.mainloop()
