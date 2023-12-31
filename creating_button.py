# Button in Tkinter
import tkinter as tk

root = tk.Tk()
def btn_function():
    lbl1 = tk.Label(root,text="Nothing but a function clicking")
    lbl1.pack(padx=30,pady=30)


btn1 = tk.Button(root,text="Button",font=25,width=20,background="black",foreground="green",padx=20,pady=20,command=btn_function)
btn1.pack()



root.mainloop()