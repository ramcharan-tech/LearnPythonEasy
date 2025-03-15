
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class CLinkedList:
    def __init__(self):
        self.head = None
    def insertCLL_End(self,data):
        temp = Node(data)
        if not self.head :
            self.head = temp
            self.head.next = self.head
        curr = self.head
        while  curr.next!= self.head:
            curr = curr.next
        curr.next = temp
        temp.next = self.head

    def printCLL(self):
        curr = self.head
        while curr.next != self.head:
            print(curr.data,"-->",end=" ")
            curr = curr.next
        else:
            print(curr.data,end=" ")
    def deletehead(self):
        if not self.head or self.head.next == self.head: return None
        curr = self.head
        while curr.next != self.head: curr = curr.next
        curr.next = self.head.next
        return curr.next  
    def deleteKNode(self,k):
        pos =1 
        if self.head == None: return None
        if k == 1:
            self.head = self.head.next
            return self.head
        curr = self.head
        for _ in range(1,k-1):
            if curr.next == self.head:
                return None
            curr = curr.next
        curr.next = curr.next.next
        return self.head
        
                




cl = CLinkedList()
cl.insertCLL_End(10)
cl.insertCLL_End(20)
cl.insertCLL_End(30)
cl.insertCLL_End(40)
cl.insertCLL_End(50)

cl.printCLL()
