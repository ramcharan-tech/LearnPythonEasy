n = int(input("num: "))
print("Oh! It's not a prime" if any(n%div==0 for div in range(2,n)) else "Yes its a Prime!")

# print("Oh! It's not a prime" if any(n % div == 0 for div in range(2, n)) else "Yes, it's a Prime!") if (n := int(input())) else None
