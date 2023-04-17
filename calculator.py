'''

Explanation:

After importing tkinter, we have defined following functions:

1. Click(num): this function takes a numeric parameter. It first converts num to string and then the function appends the string to op and displays final value of op in input area of the calculator.

2. evaluate(): This function is executed everytime the user clicks “=” i.e. when we need to evaluate the equation. Eval() is an inbuilt function in python which takes a string argument (equation) and returns a string (the output of the equation).

So this function just calls eval method and displays the output.

3. clearDisplay(): It just clears the input area.

Then we have just created an entry box to display input and output. And then finally the twelve buttons (0-9,+,-,*,/,=,C)

0-9,+,-,*,/, calls ‘click()’ when clicked.

C calls ‘clearDisplay()’.

= calls ‘evaluate()’


'''



from tkinter import *

def click(num):
    global op
    op=op+str(num)
    iptext.set(op)

def evaluate():
    global op
    output=str(eval(op))
    iptext.set(output)

def clearDisplay():
    global op
    op=""
    iptext.set(op)

calc=Tk()
calc.title("TechVidvan Calculator")
op=""

iptext=StringVar()
iparea=Entry(calc,font=('large,_font',15,'bold'),bd=10,justify="right",insertwidth=4,textvariable=iptext).grid(columnspan=10)

bt7=Button(calc,font=('arial',15,'bold'),command=lambda:click(7),bg="lavender",text="7",bd=5,padx=15,pady=10).grid(row=1,column=0)

bt8=Button(calc,font=('arial',15,'bold'),command=lambda:click(8),bg="lavender",text="8",bd=5,padx=15,pady=10).grid(row=1,column=1)

bt9=Button(calc,font=('arial',15,'bold'),command=lambda:click(9),bg="lavender",text="9",bd=5,padx=15,pady=10).grid(row=1,column=2)

add=Button(calc,font=('arial',15,'bold'),command=lambda:click('+'),bg="lavender",text="+",bd=5,padx=15,pady=10).grid(row=1,column=3)

bt4=Button(calc,font=('arial',15,'bold'),command=lambda:click(4),bg="lavender",text="4",bd=5,padx=15,pady=10).grid(row=2,column=0)

bt5=Button(calc,font=('arial',15,'bold'),command=lambda:click(5),bg="lavender",text="5",bd=5,padx=15,pady=10).grid(row=2,column=1)

bt6=Button(calc,font=('arial',15,'bold'),command=lambda:click(6),bg="lavender",text="6",bd=5,padx=15,pady=10).grid(row=2,column=2)

sub=Button(calc,font=('arial',15,'bold'),command=lambda:click('-'),bg="lavender",text="-",bd=5,padx=15,pady=10).grid(row=2,column=3)

bt1=Button(calc,font=('arial',15,'bold'),command=lambda:click(1),bg="lavender",text="1",bd=5,padx=15,pady=10).grid(row=3,column=0)

bt2=Button(calc,font=('arial',15,'bold'),command=lambda:click(2),bg="lavender",text="2",bd=5,padx=15,pady=10).grid(row=3,column=1)

bt3=Button(calc,font=('arial',15,'bold'),command=lambda:click(3),bg="lavender",text="3",bd=5,padx=15,pady=10).grid(row=3,column=2)

mul=Button(calc,font=('arial',15,'bold'),command=lambda:click('*'),bg="lavender",text="*",bd=5,padx=15,pady=10).grid(row=3,column=3)

bt0=Button(calc,font=('arial',15,'bold'),command=lambda:click(0),bg="lavender",text="0",bd=5,padx=15,pady=10).grid(row=4,column=0)

btC=Button(calc,font=('arial',15,'bold'),command=clearDisplay,bg="lavender",text="C",bd=5,padx=15,pady=10).grid(row=4,column=1)

eql=Button(calc,font=('arial',15,'bold'),command=evaluate,bg="lavender",text="=",bd=5,padx=15,pady=10).grid(row=4,column=2)

div=Button(calc,font=('arial',15,'bold'),command=lambda:click('/'),bg="lavender",text="/",bd=5,padx=15,pady=10).grid(row=4,column=3)

calc.mainloop(),
