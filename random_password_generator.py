import random

lower = "qwertyuiopasdfghjklzxcvbnm"
upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
number = "1234567890"
symbols = "[]{}()*!@#$%&_"

all = lower + upper + number + symbols

length = 16

password = "".join(random.sample(all,length))

print(password)
