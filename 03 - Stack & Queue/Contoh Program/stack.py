class Stack:
     def __init__(self):
          self.items = []  
     def isEmpty(self):
          return self.items == []  
     def push(self, item):
          self.items.append(item)  
     def pop(self):
          return self.items.pop()  
     def peek(self):
          return self.items[len(self.items)-1]  
     def size(self):
          return len(self.items)

s = Stack()
print (s.isEmpty())
s.push(4)
s.push('dog')
print (s.peek())

s.push('true')
print (s.size())
print (s.isEmpty())

s.push(8.5)
s.pop()
s.pop()
print (s.size())
print (s.items)
