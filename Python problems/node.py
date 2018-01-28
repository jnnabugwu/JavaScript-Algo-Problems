from collections import deque
class Node:#linked list#
  def __init__(self,value):
    self.value = value
    self.next = none
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
  def add(self,next):
    node = self
    while node.next != None:
      node = node.next
    node.next = next
    return True          
class Node2:#trees#
  def __init__(self,value):
    self.value = value
    self.left = None
    self.right = None
    self.leftfoot = 0
    self.rightfoot = 0
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
      else: 
        return False       
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
  def preorder(self):
    queue = deque()
    queue.append(self.root)
    while len(queue)>0:
      print(queue[0].value)
      currentnode = queue.popleft 
      if currentnode.left is not None: #error attrubute error
        queue.append(currentnode.left)
        currentnode.left.leftfoot = currentnode.leftfoot + 1
      if currentnode.right is not None:
        queue.append(currentnode.right)
        currentnode.right.rightfoot = currentnode.leftfoot + 1
 
# make an algrothim to place the nodes of the tree in columns. 
  def columns(self):
    schedule = deque()
    col = dict()
    node = self.root.value
    schedule.append(node.value)
    while len(schedule) != 0:
      if node.left:
        schedule.append(node.left)
        node.left.leftfoot = node.leftfoot + 1 
      if node.right:
        schedule.append(node.right)
        node.right.rightfoot = node.rightfoot + 1
      current = schedule.popleft()
      col[node.rightfoot - node.leftfoot] = current
      node = schedule.popleft
    return col








# tail = Node(13,None)
# body = Node(12,tail)
# head = Node(11,body)
# print(head.find(13))
# head.add(Node(14,None))
# print(body.transit())
# print(head.find(15))
seed = Tree()
(seed.insert(100))
(seed.insert(50))
(seed.insert(200))
(seed.insert(150))
# (seed.insert(80))
# (seed.insert(10))
# (seed.insert(15))
# (seed.insert(300))
# print(seed.columns())
seed.preorder()

# print(head.find(12))
# print(head.find(14))
# head.add(Node(14,None))
# print(head.find(14))
# print(head.transit())
