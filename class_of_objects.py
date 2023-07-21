class Customer:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        print("I am ",self.name,"and I am ",self.age)

c1 = Customer("PK",23)
c2 = Customer("Ravi",22)
c3 = Customer("Babe",21)

L = [c1,c2,c3]

for i in L:
    i.intro()