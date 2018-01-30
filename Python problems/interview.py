class Node:
  def __init__(self,value):
        self.value = value
        self.left = None
        self.leftfoot = 0 
        self.right = None
        self.rightfoot = 0
  def preorder(self):
      if self is None:
          return   
      queue = []
      queue.append(self)
      columns = {}
      while len(queue)>0:
      
          print(queue[0].value,queue[0].leftfoot,queue[0].rightfoot)
          currentnode = queue.pop(0)
          placer = (currentnode.rightfoot) - (currentnode.leftfoot)
          
          if placer in columns: 
              columns[placer].append(currentnode.value)
          else:
              columns[placer] = [currentnode.value]             
              
          if currentnode.left is not None: #error attrubute error
              queue.append(currentnode.left)
              currentnode.left.leftfoot = currentnode.leftfoot + 1
              currentnode.left.rightfoot = currentnode.rightfoot 
          if currentnode.right is not None:
              queue.append(currentnode.right)
              currentnode.right.rightfoot = currentnode.rightfoot + 1
              currentnode.right.leftfoot = currentnode.leftfoot
    #   c = sorted(columns.items)#keys = items
    #   for i in range(0,len(c)):
    #       print(c[i][1])
      return columns
trunk = Node(100)
trunk.left = Node(50)
trunk.left.right = Node(80)
trunk.right = Node(200)
trunk.right.left = Node(150)
trunk.right.right = Node(300)
trunk.left.left = Node(10)
trunk.left.left.right = Node(15)
print(trunk.preorder())

# years_dict = dict()
# years_dict[100] = [1]
# years_dict[100].append(2)
# years_dict[200] = 2
# years_dict[300] = [1]
# years_dict[300].append(4)
# years_dict[0] = [2,3,4]
# print(years_dict)
# b =sorted(years_dict.items())
# print(b)
# for i in range(0,len(b)) :
#     print(b[i][1])
