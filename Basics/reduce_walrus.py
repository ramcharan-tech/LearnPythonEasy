from functools import reduce

arr = [1, 2, 3, 4]

# Using a lambda function that adds two numbers: x is the accumulator, y is the new item
# reduce(function, sequence, initial_value)
result = reduce(lambda x, y: x + y, arr)
max_reduce = reduce(lambda acc, val: val if val > acc else acc, arr, float('-inf'))
print(f"result of sum using reduce is: {result}, max_val from walrus is: {max_reduce}") # Output: 10

max_val = float('-inf')
# This creates a list of "new records" and updates max_val as a side effect
[max_val := val for val in arr if val > max_val]

print(f"max_val from walrus is: {max_val}") # Output: 8

# NEXT FUNCTION EXAMPLE
numbers = [1, 3, 5, 6, 7, 8]
first_even = next((num for num in numbers if num % 2 == 0 ), None)
print(f"First even number: {first_even}") # Output: 6

#Other Examples of Walrus Operator:

# Example 1: Using walrus operator in a while loop
n = 0
while (n := n + 1) < 5:
    print(f"Current value of n: {n}")
# Example 2: Using walrus operator in list comprehension
squared_evens = [y := x**2 for x in range(10) if (y := x**2) % 2 == 0]
print(f"Squared even numbers: {squared_evens}") # Output: [0, 4, 16, 36, 64]
# Example 3: Using walrus operator in an if statement
text = "hello"
if (length := len(text)) > 3: # Assign AND Check
    print(f"String is long: {length}")

# Example 6: Using walrus operator to cache a computation
def compute_expensive_value(x):
    print("Computing expensive value...")
    return x * x
x = 5
if (expensive_value := compute_expensive_value(x)) > 20:
    print(f"Expensive value is large: {expensive_value}")   # Output: 25

# Example 7: Using walrus operator in a generator expression
gen = (y := x**2 for x in range(5) if (y := x**2) % 2 == 0)
print(f"Generator output: {list(gen)}") # Output: [0, 4, 16]

# Example 4: Using walrus operator to read input until 'exit' is entered
while (user_input := input("Enter something (type 'exit' to quit): ")) != 'exit':
    print(f"You entered: {user_input}")
