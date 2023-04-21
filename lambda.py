# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.
"""Syntax
lambda arguments : expression
The expression is executed and the result is returned:"""


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(int(input("Enter the number to be doubled: "))))
print(mytripler(int(input("Enter the number to be tripled: "))))

x = lambda a: a + 5
print(x(int(input("Enter the number to add in x: "))))

def reminder(n):
    return lambda b: b % n

togetreminderof = reminder(int(input("Enter the number by which we get reminder: ")))
print(togetreminderof(int(input("Enter the number from which we get reminder: "))))

num = [15,12,37,11,44,88]
num.pop(3)
num.sort()

print(num)

"""def myfun():
    num.copy()

myfun()"""

