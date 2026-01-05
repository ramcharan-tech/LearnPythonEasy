n = int(input()) # Find prime or composite
if any(n % divisor == 0 for divisor in range(2,n//2)):
    print(n,"is composite")
else:
    print(n,"is prime number")