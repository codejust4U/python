### Inheritence
"""
class User:
    def login(self):
        print("User logged in")

    def regeister(self):
        print("Register")



class Student(User):
    def enroll(self):
        print("Enroll")
    def review(self):
        print("review")



st = Student()
st.enroll()
st.review()
st.login()
st.regeister()
"""

"""
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.price =price
        self.brand = brand
        self.camera = camera


class Smartphone(Phone):
    pass

s = Smartphone(20000,"IOs",13)
print(s.brand)"""


"""

The code will crash here coz child class cant access the hidden members of the parent class

class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.price =price
        self.__brand = brand
        self.camera = camera


class Smartphone(Phone):
    pass

s = Smartphone(20000,"IOs",13)
print(s.__brand)"""


"""
Method overriding

It will choose the child defintion if same function is availabe in both child and parent

class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.price =price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buyinga phon")


class Smartphone(Phone):
    
    def buy(self):
        print("Buying a smartphone")
        print("Buying a smartphone")

s = Smartphone(20000,"IOs",13)

s.buy()"""



"""
class Parent:
    def __init__(self,num):
        self.__num = num
        

    def get_num(self):
        return self.__num
    

class child(Parent):
    def show(self):
        print("child class")


son = child(100)
print(son.get_num())

son.show()"""



