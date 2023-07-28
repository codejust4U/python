class stack:
    def __init__(self, size):
        self.size = size
        self.__stack = [None] * self.size
        self.top = -1

    def push(self, value):
        if self.top == self.size-1:
            return 'Overflow'
        else:
            self.top += 1
            self.stack[self.top] = value

    def pop(self):
        if self.top == -1:
            return 'Underflow'
        else:
            data = self.stack[self.top]
            self.top -=1
            print(data)

    def traverse(self):
        for i in range(self.top+1):
            print(self.stack[i],end='')



s = stack(3)

print(s.stack)

s.push(4)
s.push(5)
s.push(6)


s.pop()

s.pop()

s.pop()


s.traverse()

s.push(5)