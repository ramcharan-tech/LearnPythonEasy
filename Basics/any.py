n = int(input())
if any(n % divisor == 0 for divisor in range(2,n)):
    print(n,"is composite")
else:
    print(n,"is prime number")