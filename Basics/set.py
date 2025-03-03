"""
Sets in Python are mutable, meaning their contents can be changed after creation. However, the elements within a set must be immutable.
If you need an immutable set, you can use a frozenset. frozenset objects are immutable versions of sets, and they can be used as elements within other sets or as keys in dictionaries.
"""
x= {1,2,3,4}
print(x)
print(4 in x) # Best for lookups O(1)

empty_set = set() # it cannot be {}

#crud
x.add(5)
x.update(empty_set) # value can be lists,tuples,sets etc..
removedvalue=x.discard(5)
print(removedvalue)

x.pop()	# Removes and returns an arbitrary set element. Raises KeyError if the set is empty
x.remove(4)	# Removes an element from the set. If the element is not a member, raises a KeyError
x.clear()

# other functions all,any,enumerate,len,max,min,sorted,sum.
# A | B (A.union(B)), A&B (A.intersection(B)),A-B A.difference(B),A ^ B A.symmetric_difference(B) (Xor operation has no common elements),
# A==B (if containes same elments any order),_update will update he same set.
# .isdisjoint(),.issubset(),.issuperset()
