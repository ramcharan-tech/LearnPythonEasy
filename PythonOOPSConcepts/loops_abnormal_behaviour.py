x = [1,2,3,4,5]
count = 0
for i in x:
    if i%2==0:        
        x.remove(i)
    count += 1
    print(i)
print("total iterations are:",count)
