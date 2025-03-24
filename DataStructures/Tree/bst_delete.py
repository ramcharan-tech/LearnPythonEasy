import math
class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class Tree:
    def __init__(self,root=None):
        self.root = root
    def insert(self,data,parent,isright=0):
        temp = Node(data)
        if not self.root: 
            self.root = temp
            return temp
        if not isright:  parent.left =temp
        else: parent.right = temp
        return temp


tree = Tree()
r = tree.insert(10,None)
tl1=  tree.insert(20,r)
tr1 = tree.insert(30,r,1)
trf2 = tree.insert(40,tr1)
trr2 = tree.insert(50,tr1,1)
