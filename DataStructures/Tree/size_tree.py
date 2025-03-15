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
    def size(self,r):
        if not r: return 0
        sz = 0
        sz+= self.size(r.left)
        sz+=1
        sz+= self.size(r.right)
        return sz

size = lambda r : 0 if not r else size(r.left)+1+size(r.right)
tmax = lambda r : -math.inf if not r  else max(tmax(r.left),r.data,tmax(r.right))
tsearch = lambda r,k : False if not r  else any([tsearch(r.left,k),r.data==k,tsearch(r.right,k)])


tree = Tree()
r = tree.insert(10,None)
tl1=  tree.insert(20,r)
tr1 = tree.insert(30,r,1)
trf2 = tree.insert(40,tr1)
trr2 = tree.insert(50,tr1,1)
print(tree.size(r))
print(size(r))
print(tmax(r))
print(tsearch(r,10))

# gpt code #TODo
search = (lambda k: (lambda r: False if not r else any([t(r.left), r.data == k, t(r.right)]))) 
t = lambda r: search(r)
root = Node(5, Node(3, Node(1), Node(4)), Node(7, Node(6), Node(8)))
srch = search(10)
print(srch(r))

        