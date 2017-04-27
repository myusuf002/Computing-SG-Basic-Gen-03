#1. buat fungsi hitung depth
#2. buat fungsi print Level Order
    #23 10 65 16 45 67 19 24 30

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

  def countDepth(self):
    if(self == None): return -1
    else:
      if(self.left.countDepth != None):
        return self.left.countDepth
      else:
        return self.right.countDepth

T = Node(23)   
T.insertNode(10)
T.insertNode(16)
T.insertNode(19)
T.insertNode(65)
T.insertNode(45)
T.insertNode(24)
T.insertNode(50)
T.insertNode(67)

T.preOrder()
print ("\nDepth :",T.countDepth())
