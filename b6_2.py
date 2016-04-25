
class EmptyStackError(Exception):
    def __init__(self):
        super().__init__("Stack underflow!")


class FullStackError(Exception):
    def __init__(self):
            super().__init__("Stack overflow!")


# A simple stack in python with ints.
class Stack():
    def __init__(self, max_size=8):
        self.max_size = max_size
        self.data = []

    def is_empty(self):
        if len(self.data) == 0:
            return True

    def is_full(self):
        if len(self.data) == self.max_size:
            return True

    def push(self, data):
        if not self.is_full():
            self.data.append(data)
            return data
        else:
            raise FullStackError()

    def pop(self):
        if not self.is_empty():
            output = self.data[len(self.data) -1]
            del self.data[len(self.data) -1]
            return output
        else:
            raise EmptyStackError()  

    def peek(self):
        if self.data == []:
            print("Stack Underflow!")
        else:
            return self.data[len(self.data)-1] 


s=Stack()

print(s.push('dog'))
print(s.push('python1'))
print(s.push('python2'))
print(s.push('python3'))
print(s.push('python4'))
print(s.push('python5'))
print(s.peek())
print(s.push(8.4))
print(s.push('python6'))
print(s.push('python7'))
print(s.push('python8'))
print(s.push('python9'))
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())        
