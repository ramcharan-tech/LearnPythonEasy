# list are mutable
x = [1,2,3]
y =x[:] #copy
z=x #ref
x[0]='hello'
print(x,y,z)