#BINARY SEARCH TREE
#deklarasi Node
class Node:
  def __init__(self, val):
    self.info = val
    self.left = None
    self.right = None

  def insertNode(self, val):
    if(val < self.info):
      if(self.left == None): self.left = Node(val)
      else: self.left.insertNode(val)
    elif(val > self.info):
      if(self.right == None): self.right = Node(val)
      else: self.right.insertNode(val)

  def inOrder(self):
    if(self.left): self.left.inOrder()
    print(self.info, end=" ")
    if(self.right): self.right.inOrder()

  def preOrder(self):
    print(self.info, end=" ")
    if(self.left): self.left.preOrder()
    if(self.right): self.right.preOrder()

  def postOrder(self):
    if(self.left): self.left.postOrder()
    if(self.right): self.right.postOrder()
    print(self.info, end=" ")

  def searchNode(self, val):
    if(val < self.info):
      if(self.left): return self.left.searchNode(val)
      else: return False
    elif(val > self.info):
      if(self.right == None): return self.right.searchNode(val)
      else: return False
    else: return True
   
T = Node(23)
T.insertNode(10)
T.insertNode(16)
T.insertNode(19)
T.insertNode(65)
T.insertNode(45)
T.insertNode(24)
T.insertNode(50)
T.insertNode(67)

T.inOrder()
print()
T.preOrder()
print()
T.postOrder()
print()

print (T.searchNode(12))
print (T.searchNode(10))
