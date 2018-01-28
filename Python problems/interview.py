class Node:
  def __init__(self,value):
        self.value = value
        self.left = None
        self.leftfoot = 0
        self.right = None
        self.rightfoot = 0
  def preorder(self):


      #Base case
      if self is None:
          return   
      queue = []
      queue.append(self)
      columns = {}
      while len(queue)>0:
      
          print(queue[0].value,queue[0].leftfoot,queue[0].rightfoot)
          currentnode = queue.pop(0)
          placer = int((currentnode.rightfoot) - (currentnode.leftfoot))
          if placer in columns: # how do i add a number to a list inside of a dictonary
              columns[placer] = currentnode.value
          else:
              columns[placer] = currentnode.value             
              
          if currentnode.left is not None: #error attrubute error
              queue.append(currentnode.left)
              currentnode.left.leftfoot = currentnode.leftfoot + 1
              currentnode.left.rightfoot = currentnode.rightfoot 
          if currentnode.right is not None:
              queue.append(currentnode.right)
              currentnode.right.rightfoot = currentnode.rightfoot + 1
              currentnode.right.leftfoot = currentnode.leftfoot
      return columns
trunk = Node(100)
trunk.left = Node(50)
trunk.left.right = Node(80)
trunk.right = Node(200)
trunk.right.left = Node(150)
row = {}
row[trunk.leftfoot-1] = trunk.value
trunk.preorder()