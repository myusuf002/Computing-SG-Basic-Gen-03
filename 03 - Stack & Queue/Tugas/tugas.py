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

inputan = "))(("

for x in inputan:
     if (x == "("):
          s.push(x)
     elif (x == ")"):
          # s.pop()
          if (s.isEmpty()):
                cek = False
          else:
               s.pop()

if (s.isEmpty() == True) and (cek == True):
     print(inputan, " VALID BGT IH")
elif (s.isEmpty() == False) or (cek == False):
     print(inputan, " NOT VALID BOSS")
