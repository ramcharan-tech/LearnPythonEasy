# list are mutable,ordered, dynamic size, different types can be stored
x = [1,2,3]
y =x[:] #copy
z=x #ref
x[0]='hello'
print(x,y,z)
l = "axz"

# convert to list
result = print(list(l))
#List functions
x.append(4)
x.insert(4,5) # first parameter is index
k = [6,7]
x.extend(k) # m =x+k or m = [p for p in x]+ [l for l in k] or m = [*x,*k] To merge
print(4 in x)
print(x)
print(x.index(4)) #may get error
print(x.count(4)) # count a given element
print(x.index(4,0,4))

x.remove(4) #may get error # to remove an element 4
print(x.pop()) # pop(1)
del x[2]
del x[0:2]

print("list is:",x)
print(max(x), min(x), sum(x))
x.sort()
x.reverse()






a = 2
b= a
a = 5
print(a,b) # so integers are not referenced