print("---------------------------Operaor in python-----------------------------")
"""
----------------------------Operators in python-----------------------------------
In Python programming, Operators in general are used to perform operations on values and variables. These are standard symbols used for the purpose of logical and arithmetic operations. In this article, we will look into different types of Python operators. 

OPERATORS: These are the special symbols. Eg- + , * , /, etc.
OPERAND: It is the value on which the operator is applied.
"""
op1 = int(input("Enter the operands: "))
op2 = int(input("Enter the operands: "))

def sum(op1,op2):
    return op1 + op2

def sub(op1,op2):
    return op1-op2
def mul(op1, op2):
    return op1 * op2

def div(op1,op2):
    return op1/op2

print(sum(op1,op2))
print(sub(op1,op2))
print(mul(op1,op2))
print(div(op1,op2))

print("---------------------------Operaor precedence-----------------------------")

"""
----------------------------Operators precedence----------------------------
Operator precedence is defined as the priority order of execution of operators in the programs. This is as same as the BODMAS rule i.e:
B- Bracket ()
O- Of/Exponentation ^
D- Division /
M- Multiplication *
A- Addition +
S- Subtraction -
"""

a = (3*2)+4-6/3
print(a)

print("--------------------------Conditional statements------------------------------")
"""
----------------------------Conditional Statements----------------------------
Conditional statements are the statements which alter the flow of execution of program.
Basic python conditional statements
1. If statement: The if statement is used to test a particular condition and if the condition is true, it executes a block of code known as if-block. 

2. Elif Statement: The if-else statement provides an else block combined with the if statement which is executed in the false case of the condition. If the condition is true, then the if-block is executed. Otherwise, the else-block is executed.

3. If - else statement: The elif statement enables us to check multiple conditions and execute the specific block of statements depending upon the true condition among them.
"""


def result(marks):
    if marks >= 90:
        return "Excellent"
    elif marks > 80 and marks < 90:
        return "Very Good"
    elif marks > 40 and marks < 80:
        return "Acceptable"
    else:
        return "Bad"


print(result(int(input("Enter the marks: "))))

print("--------------------------Loops------------------------------")
"""
----------------------------Loops in python----------------------------
In python, loop is used to execute a block of statements repeatedly until a given condition is satisfied.
Basic loops in python are: 
1. While loop: With the while loop, we can execute a set of statements as long as a condition is true.

2. For loop: A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
"""

print("--------------------------While Loops------------------------------")
def while_loop():

    i = 1
    while i < 5:
        print(i)
        i += 1
while_loop()


print("---------------------------For loop-----------------------------")
for i in range(1,5):
    print(i)




print("------------------------Break and Continue--------------------------------")
"""
----------------------------Break and Continue----------------------------
1. Break statement in Python is used to bring the control out of the loop when some external condition is triggered. 

2. Break statement is used to skip the execution of statement when condition met

"""
for i in range(0,9):
    if i == 3:
        break

    print(i)

print("--------------------------------------------------------")

for i in range(0,9):
    if i == 6:
        continue
    print(i)

print("--------------------------------------------------------")
