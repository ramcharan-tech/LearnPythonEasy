# https://www.programiz.com/python-programming/methods/built-in/bin
# https://www.geeksforgeeks.org/python-dsa-libraries/

import array
from collections import deque, Counter, ChainMap, defaultdict,OrderedDict
from queue import Queue
import heapq
from treelib import Node, Tree
import bisect
from intervaltree import IntervalTree, Interval
from pygtrie import Trie # getting error
import math

def arraydef():
    int_array = array.array('i', [1, 2, 3, 4, 5])
    int_array.extend({6,7,8})
    print(int_array.itemsize)
    print(int_array.buffer_info())
    print(int_array.count(2))
arraydef() # need to call after the method is implemented
def dequedef(): # can add/remoe from front and rear
    my_queue = deque()
    my_queue.append(1)
    my_queue.appendleft(2)
    elep = my_queue.pop() # or use popleft
    my_queue.remove(2) # remove doesn'return any ele
    my_queue.extend({3,4})
    print("from deque: ",elep,my_queue.index(3))
    print(my_queue)
dequedef()
def queuedef(): # can add from rear and remove from front
    myq = Queue()
    myq.put(1)
    myq.put(2)
    ele=myq.get() # removes and return the first element
    print(myq.full(), myq.empty(),myq.qsize(),myq.maxsize)
    # while not myq.empty():
    #     print(myq.get())
    print(2 in list(myq.queue))
    print([i for i in list(myq.queue)])
queuedef()

# Counting the occurrences of elements in a collection (e.g., a list or a string)
my_list = ['apple', 'banana', 'apple', 'orange', 'apple', 'banana']
my_counter = Counter(my_list)
print("printing: " ,[i for i in my_counter.elements()])

print(my_counter,my_counter.most_common(2),my_counter.total(),sep="\n")
# other methods subtract.update,fromkeys