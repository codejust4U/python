# using grid

import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Label name",font=('Georgia',25))
label1.grid(row=2,column=1)

root.mainloop()