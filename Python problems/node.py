class Node:
  def __init__(self,value,next):
    self.value = value
    self.next = next
  def transit(self):
    node = self
    while node.next != None:
      print(node.value)
      node = node.next
      if node.next == None:
        return(node.value)
  def find(self,seek):
    node  = self
    if node.value == seek:
      return True
    while node.next != None:
      if node.value == seek:
        return True
      else:
        node = node.next
    if node.value == seek:
      return True
    else:
      return False
  def add(self,Node):
    node = self
    while node.next != None:
      node = node.next
    node.next = Node
    return node.next          
class Node2:
  def __init__(self,value):
    self.value = value
    self.left = None
    self.right = None
  def insert(self,data):
    if self.value == data:
      return False
    elif self.value > data:
      if self.left:
        return self.left.insert(data)
      else:
        self.left = Node2(data)
        return True
    else:
      if self.right:
        return self.right.insert(data)
      else:
        self.right = Node2(data)
        return True
  def find(self, data):
    if(self.value == data):
      return True
    elif self.value > data:
      if self.left:
        return self.left.find(data)
      else:
        return False
    else:
      if self.right:
        return self.right.find(data)       

class Tree:
  def __init__(self):
    self.root = None
  
  def insert(self,data):
    if self.root:
      return self.root.insert(data)
    else:
      self.root = Node2(data)
      return True
  def find(self,data):
    if self.root:
      return self.root.find(data)
    else:
      return False




tail = Node(13,None)
body = Node(12,tail)
head = Node(11,body)
print(head.find(13))
head.add(Node(14,None))
print(body.transit())
print(head.find(14))
# print(head.find(12))
# print(head.find(14))
# head.add(Node(14,None))
# print(head.find(14))
# print(head.transit())
