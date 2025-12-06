matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# change below code to flatten only prime numbers
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

flattened = [item for sublist in matrix for item in sublist if is_prime(item)]
print(flattened)
