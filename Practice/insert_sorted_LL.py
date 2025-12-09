class Node:
    def __init__(self,key):
        self.key = key
        self.next = None

def insertatend(head,key):
    if head ==None:
        return Node(key)
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = Node(key)
    return head

def insertsorted(head,key):
    temp = Node(key)
    if head == None: return temp
    elif head.key > key:
        temp.next = head
        return temp
    curr = head
    while curr.next != None and curr.next.key < key:
        curr= curr.next    
    temp.next = curr.next
    curr.next = temp
    return head
def printLL(head):
    curr = head
    while curr!=None:
        print(f"{curr.key}-->",end=" ")
        curr = curr.next
    print()

def reverseLL(head):
    if head == None: return None
    prev = None
    curr = head
    while curr!=None:        
        temp  = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev
def recursive_reverseLL(head):
    if not head or not head.next: return head
    rec_head = recursive_reverseLL(head.next)
    rec_tail = head.next
    rec_tail.next = head
    head.next = None
    return rec_head
def recursive_reverseLL2(head,prev=None):
    if not head: return prev #base condition    
    next = head.next
    head.next = prev
    return recursive_reverseLL2(next,head)

h = insertsorted(None, 30)
h = insertsorted(h,20)
h = insertsorted(h,10)
h = insertsorted(h,50)
printLL(h)
h = reverseLL(h)
printLL(h)
h = recursive_reverseLL(h)
printLL(h)
h = recursive_reverseLL2(h)
printLL(h)