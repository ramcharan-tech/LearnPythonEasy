class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,data):
        node = Node(data)
        if self.head==None:
            self.head = node
            self.tail = node
        self.tail.next = node
        self.tail = node
    
    def display(self):
        h = self.head
        while h is not None:
            print(h.data)
            h = h.next
       
ll = linkedList()
ll.append(6)
ll.append(5)
ll.append(4)
ll.append(3)
ll.display()
