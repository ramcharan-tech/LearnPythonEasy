n = int(input("num: "))
print("composite" if any(n%div==0 for div in range(2,n/2)) else "prime")

# print("Oh! It's not a prime" if any(n % div == 0 for div in range(2, n)) else "Yes, it's a Prime!") if (n := int(input())) else None

arr = [1,2,3]
print(sum(arr[0:1]))