# constructor, insert, extract min, decrease key, delete,construction (enhanced with build heap)
# left child,right child,parent,min heapify

class minheap:
    def __init__(self):
        self.arr = []
    parent = lambda i : i-1//2
    lchild = lambda i : 2*i+1
    rchild = lambda i : 2*i+2
    def insert(self,x): #O(logn)
        self.arr.append(x)        
        i= len(self.arr)-1
        p = self.parent(i)
        while i > 0 and self.arr[p]> self.arr[i]:
            self.arr[p],self.arr[i] = self.arr[i],self.arr[p]
            i =p
            p = self.parent(i)

    def minheapify(self):
        pass
    def extractmin(self):
        pass
    def decreasekey(self):
        pass
    def delete(self,x):
        pass

mh =minheap()
mh.arr = [10,20,15,40,100,25,45]
mh.insert(12)
print(mh.arr)

