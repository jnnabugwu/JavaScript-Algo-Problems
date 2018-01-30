class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.leftfoot = None#coordinates
        self.rightfoot = None#coordinates
    
    def preordercols(self):
        #Base case
        if self is None:
            return

        schedule = []
        schedule.append(self)
        columns = {}
        while len(schedule) > 0:
            print(schedule[0].value,schedule[0].leftfoot,schedule[0].rightfoot)
            currentnode = schedule.pop(0)
            placer = currentnode.rightfoot - currentnode.leftfoot
            columns[placer] = currentnode.value
            if placer in columns:
                columns[placer].append(currentnode.value)
                else:
                    columns[placer] = [currentnode.value]

            if currentnode.left:
                schedule.append(currentnode.left)
                currentnode.left.leftfoot =  currentnode.leftfoot + 1
                currentnode.left.rightfoot = currrentnode.rightfoot
            if currentnode.right:
                schedule.append(currentnode.right)
                currentnode.right.rightfoot = current.rightfoot + 1
                currentnode.right.leftfoot = current.leftfoot
        return columns

trunk = Node(100)
trunk.left = Node(50)
trunk.right = Node(200)
trunk.left. = Node()
            
