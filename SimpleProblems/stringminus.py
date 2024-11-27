s1,s2 = input("Enter the first string:"),input("Enter the second string:")

def checkorder(s1, s2):
    if len(s1)!=len(s2):
      return -1
    res = (ord(s2[0])-ord(s1[0])+26)%26
    for i in range(1,len(s1)):
        if res != (ord(s2[i])-ord(s1[i])+26)%26:
          return -1
    return res      
print(checkorder(s1, s2))