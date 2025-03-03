#tuple is immutable means Once a tuple is created, its elements cannot be changed, added, or removed
# useful in such as representing fixed collections of items or using them as keys in dictionaries.
""" 
https://www.geeksforgeeks.org/python-tuple-methods/
https://www.programiz.com/python-programming/tuple
"""
singletuple = ('Hello',) # comma should be present otherwise it will be string
x = (0,1,2,3) # or tuple((0,1,2,3))
print(x.count(2),len(x)) # count occurences of given value and second arg is find length of tuple
complexval = ((0,1),[1,2])
print(complexval.count((0,1)),complexval.count([1,2])) # it can count complex types as well
# tuple.index(element, start(opt), end(opt)) --> returns the first occurrence of the given element &  raises a ValueError if the element is not found
# deleting the entire tuple
del x,complexval