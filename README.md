# LEARN PYTHON EASY WAY
This repository talks about Basics, DS and Algorithms, Notes etc...

Fundamental Notes:

1. The else block will not execute if the for loop is stopped by a break statement.
1. global global_var --> to modify global var in local function similarly nonlocal can be used if you need to resuse in nested function.
1. The for loop is usually used when the number of iterations is known. For example,
1. pass statement is a null statement which can be used as a placeholder for future code
1. Every recursive function must have a base condition that stops the recursion. By default, the maximum depth of recursion is 1000. If the limit is crossed, it results in RecursionError
1. recursive are expensive but readable
1. is -> identical or not, in ,Not in -> membership operator
1. import moduels `import math as m ` , `from math import pi`, dir() list all functions. While importing packages, Python looks in the list of directories defined in sys.path, similar as for module search path.
1. when converting from float to integer, the number gets truncated (decimal parts are removed).
1. we can also create tuples without using parentheses.use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types. Iteration using tuple is faster than list because of its immutability. can use tuples as key in dictionary.
1. In Python, strings are immutable.
   # multiline string 
message = """
Never gonna give you up
Never gonna let you down
"""
1. index vs find , the latter will not throw error it gives -1 if not found.


| Data Structure | Ordered | Mutable | Iterable | Duplicate Elements | Indexing |
|----------------|---------|---------|----------|--------------------|----------|
| List           | Yes     | Yes     | Yes      | Yes                | Yes      |
| Tuple          | Yes     | No      | Yes      | Yes                | Yes      |
| Range          | Yes     | No      | Yes      | No                 | Yes      |
| Set            | No      | Yes     | Yes      | No                 | No       |
| Dictionary     | No      | Yes     | Yes      | No (keys)          | Keys     |
| Stack	         | Yes	   | Yes	 | Yes	    | Yes	             | Yes      |
| Queue	         | Yes	   | Yes	 | Yes	    | No	             | Yes      |
| Heap	         | No	   | Yes	 | No	    | No	             | No       |
| Linked List	 | Yes	   | Yes	 | No	    | Yes	             | No       |


1. List: A list is a collection of elements that are ordered, mutable, and can contain duplicate elements. Lists are indexed and iterable. They are created using square brackets [] or the list() constructor . functions --> append,extend,insert,remove,pop,del,clear,count,index,sort,reverse,copy. while sorted returns new list without affecting current list
    list.sort(key=function, reverse=False)
    sorted(list, key=function, reverse=False)
2. Tuple: A tuple is a collection of elements that are ordered, immutable, and can contain duplicate elements. Tuples are indexed and iterable. They are created using parentheses () or the tuple() constructor. If there is one element use var3 = "hello". my_tuple[:-7] or my_tuple[:len(my_tuple)-7] is same.
3. Range: A range is a collection of elements that are ordered, immutable, and do not contain duplicate elements. Ranges are indexed and iterable. They are created using the range() constructor 
4. Set: A set is a collection of elements that are unordered, mutable, and do not contain duplicate elements. Sets are not indexed but are iterable. They are created using curly braces {} or the set() constructor. func --> add,update,discard,clear,copy,all,any,enumerate,len,min,max,sorted,sum,union,intersection,difference,differnce_update,intersection_update,symetric_difference,isdisjoint,issubset,issuperset,pop,remove,symmetric_difference_update, |&-^=
5. Dictionary: A dictionary is a collection of key-value pairs that are unordered, mutable, and do not contain duplicate keys. Dictionaries are not indexed but are iterable. They are created using curly braces {} or the dict() constructor . func --> update,pop,clear,keys,values,get,popitem,copy
6. Stack: A stack is a collection of elements that are ordered, mutable, and follow the Last-In-First-Out (LIFO) principle. Stacks are indexed and iterable. They are created using the list() constructor 
7. Queue: A queue is a collection of elements that are ordered, mutable, and follow the First-In-First-Out (FIFO) principle. Queues are indexed and iterable. They are created using the deque() constructor from the collections module 
8. Heap: A heap is a collection of elements that are unordered, mutable, and follow a specific ordering principle. Heaps are not indexed but are iterable. They are created using the heapq module 
9.  Linked List: A linked list is a collection of elements that are ordered, mutable, and can contain duplicate elements. Linked lists are not indexed but are iterable. They are created using the LinkedList() constructor from the collections module 
10. String: funcitons--> upper,lower,partition(returns tuple),replace,find,rstrip,split,startwith,isnumeric,index,rindex