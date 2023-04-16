class Shape: 
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        print(self.width*self.height)

class Rectangle(Shape):
    #your code goes here
    def perimeter(self):
        print(2*(self.height+self.width))

w = int(input())
h = int(input())

r = Rectangle(w, h)
r.area()
r.perimeter()
