for i in range(1,10,2): # for loop is usually used in the sequence when the number of iterations is known
    if i==5:
       continue
    if i==11:
       break
    print("odd element: {}".format(i))
else:
   print("loop not break")
#------------------------------------------------------------ 
x = [1,2,3,"x"]
for _,element in enumerate(x): # enumerate to get index and element
  print(_,element) # _ is also a varaible
#--------------------------------------------------------
x=0
while x < 10: # when the number of iterations is unknown
    x=x+1
    print(x)
else:
   print("while loop hasn't broken")