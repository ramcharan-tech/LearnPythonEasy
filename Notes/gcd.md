
GCD(A, B) = GCD(B, A % B) \
(where % is the modulus operator)\
Whenever a problem involves repeatedly reducing a number in a structured manner, it's worth checking if it follows the GCD pattern.
Q1:You need to find the largest common unit that can divide two numbers.
Q2:A problem involves iterative subtraction or modulus operations.
Q3:You need to normalize two values in the simplest ratio.

1. Finding LCM (Least Common Multiple) Using GCD
✅ Problem: Find the LCM (Least Common Multiple) of two numbers.
LCM(A,B)= A*B/GCD(A,B)

import math
def lcm(a, b):
    return (a * b) // math.gcd(a, b)

print(lcm(12, 18))  # Output: 36
This is useful in problems involving common multiples in scheduling, tiling, and repeating patterns.
4. Simplifying Fractions
✅ Problem: Given a fraction P/Q, reduce it to its simplest form.
✅ Solution: Divide both numerator and denominator by GCD(P, Q).
import math
def simplify_fraction(P, Q):
    gcd = math.gcd(P, Q)
    return P // gcd, Q // gcd

print(simplify_fraction(8, 12))  # Output: (2, 3)
5.✅ Problem: You have N items and M people. Find the largest group size where each person gets the same number of items.
  ✅ Solution: The answer is GCD(N, M).
If a problem involves finding cycles, ratios, or equivalences, LCM (which depends on GCD) can be useful.

Note: **mid = lo + hi >> 1 is a shorter/faster operation to write mid = (lo + hi) // 2.**

LeetCode 1447 - Simplified Fractions
LeetCode 1201 - Ugly Number III Inclusion-Exlusion Counting
