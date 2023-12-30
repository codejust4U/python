# changing default position
from tkinter import *

# changing the default output position
import tkinter as tk

root = tk.Tk()

root.geometry("%dx%d+%d+%d" %(500,300,5,5))  #after width the 5 and 5 are x-axis and y-axis

root.mainloop()