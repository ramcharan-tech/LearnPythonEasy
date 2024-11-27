x=input()

def palindrome(x):
    if x == x[::-1]:
      print("Yes! Its a plaindorme")
    else:
        print("No! Its not a plaindorme")
      
def reverse(x):
    y=""
    l=len(x)
    for i in range(1,l+1):
        y+=x[l-i]
    return y
palindrome(x)
