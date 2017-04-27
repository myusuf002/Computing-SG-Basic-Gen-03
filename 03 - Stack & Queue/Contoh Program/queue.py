class Queue: 
    def __init__(self):
        self.items=[] 
    def isEmpty(self):
        return self.items==[] 
    def enqueue(self,item):
        self.items.insert(0,item) 
    def dequeue(self):
        return self.items.pop() 
    def size(self):
        return len(self.items)
    def getList(self):
        return self.items

q = Queue()
print (q.isEmpty())
q.enqueue(4)
q.enqueue('dog')
q.enqueue('true')
print (q.size())

print (q.isEmpty())
q.enqueue(8.5)
q.dequeue()
q.dequeue()
print (q.size())
print (q.items)
