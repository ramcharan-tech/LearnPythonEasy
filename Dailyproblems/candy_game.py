"""Candy Game

There are two people, A and B.
Person A has ‘X’ candies and B has ‘Y’ candies.
The person with fewer candies eats the same number of candies he has from another person's collection of candies.
This game continues until they have an equal number of candies or at least one of them is left with zero candies.

Find the total number of candies left at the end of the game.

Note
X and Y are non-negative integers.

Example
If A has 2 candies and B has 6 candies, A will eat 2 candies of person B. 
 
Function Description
In the provided code snippet, implement the candygame(...) method using the variables to find the total number of candies left at the end of the game. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”.

There will be multiple test cases running so the Input and Output should match exactly as provided.
The base Output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables.

Input Format
The input contains 2 space-separated integers, X and Y, denoting person A's number of candies and person B's number of candies.

Sample Input

5 3    -- denotes X and Y
 
Constraints
1 <= X, Y <= 106

Output Format
The output contains a single integer denoting the total number of candies left at the end of the game.

Sample Output
2
 
Explanation
X = 5, Y = 3.
Person A has 5 candies; Person B has 3 candies. So, B eats 3 candies of A.
 
X = 2, Y = 3
Person A has 2 candies; Person B has 3 candies. So, A eats 2 candies of B.
 
X = 2, Y = 1
Person A has 2 candies; Person B has 1 candy. So, B eats 1 candy of A.
 
X = 1, Y = 1
Each one has equal candies, i.e., 1, so the game ends.
The total number of candies left at the end of the game is 2 ( X = 1, Y = 1).
Hence, the output is 2.
"""
import math

def candygame(X,Y):
    # this is default OUTPUT. You can change it.
    result = -404

    gcd_value=math.gcd(X,Y) # Euclidean algorithm and The game reduces the larger number by the smaller one repeatedly, which is exactly how the GCD algorithm works.
    #Once both numbers are equal, they must be GCD(X, Y).
    #####--------------- Finding least or greatest repetitions of patterns use GCD #####-------------------------------------
    result=gcd_value

    # write your Logic here:

    return 2*result


# INPUT [uncomment & modify if required]
X,Y = input().split()
X = int(X)
Y = int(Y)

# OUTPUT [uncomment & modify if required]
print(candygame(X,Y))

