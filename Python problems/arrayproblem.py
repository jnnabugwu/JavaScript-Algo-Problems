#Given a sorted array in increasing value. place the elements in the array in a tree with minimum hieght
#4.3 in cracking the code interview.
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.branch = 0 #this is for problem 4.1 check if a given tree is balanced
    def insertarray(self,array):
        if len(array) < 1:
            return False
        if len(array) == 2:
            node = Node(array[0])
            node.left = Node(array[1])
        if len(array) == 3:
            node = Node(array[0])
            node.left = Node(array[1])
            node.right = Node(array[2])
            print(node.value,node.left.value,node.right.value)            
        for i in range(0,len(array)//2):
            z = 1 + 2*i
            node = Node(array[i])
            node.left = Node(array[z])
            node.right = Node(array[z+1])
            print(node.value,node.left.value,node.right.value)
        return True
#check if a tree is balanced
    def balanced(self):
        schedule = []
        leaf = []
        schedule.append(self)
        while len(schedule) > 0:
            currentnode = schedule.pop(0)
            if currentnode.left != None:
                currentnode.left.branch = currentnode.branch + 1
                schedule.append(currentnode.left)
            if currentnode.right != None:
                currentnode.right.branch = currentnode.branch + 1
                schedule.append(currentnode.right)
            if currentnode.right == None and currentnode.left == None:
                leaf.append(currentnode.branch)
        difference = 0        
        for i in range(1,len(leaf)):
            if abs(leaf[i] - leaf[i-1]) > difference:
                difference = abs(leaf[i] - leaf[i-1])
        return difference < 2

            


seed = Node(0)
seed.insertarray([1,2,3,4,5,6,7])
print(seed.balanced())



