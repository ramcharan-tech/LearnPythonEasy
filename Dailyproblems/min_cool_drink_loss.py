"""We fill the table from smaller subproblems (base cases) to larger subproblems."""

def findMinLoss_iterative(N,A):
    dp = [[0] * N for _ in range(N)]
    for l in range(0,N): # l represents the subproblem size
        for i in range(N-l): # i is the left index
            j = i +l # j is the right index
            K = N-(j-i)
            if i == j:
                dp[i][j] = K * A[i]
            else:
                dp[i][j] = min(K*A[i]+dp[i+1][j], K*A[j]+dp[i][j-1])
    return dp[0][N-1]

import sys
from functools import lru_cache
def find_min_loss(A, N):
    @lru_cache(None)
    def helper(left, right):
        if left > right: # Base case, last condition
            return 0
        day = N-(right-left)
        sell_left = day * A[left] + helper(left + 1, right)
        sell_right = day * A[right] + helper(left, right - 1)
        
        return min(sell_left, sell_right)
    
    return helper(0, N - 1)

def findMinLoss_brute_force(N, A): # same as above method without lru_cache
    def dfs(i, j, k):
        if i > j:
            return 0  # Base case: No more drinks left
        return min(
            k * A[i] + dfs(i + 1, j, k + 1),  # Selling the first drink
            k * A[j] + dfs(i, j - 1, k + 1)   # Selling the last drink
        )
    
    return dfs(0, N - 1, 1)

def findMinLoss_hashmap(N, A):
    memo = {}  # Hash map for memoization

    def dp(left, right):
        if left > right:
            return 0 
        if (left, right) in memo:
            return memo[(left, right)] 
        
        days = N - (right - left)
        
        # Base case: Only one drink left
        if left == right:
            memo[(left, right)] = days * A[left]
            return memo[(left, right)]
        memo[(left, right)] = min(
            days * A[left] + dp(left + 1, right), 
            days * A[right] + dp(left, right - 1)
        )
        return memo[(left, right)]

    return dp(0, N - 1)

# Sample Input
N = 3
A = [10, 20, 30]
print("iterative: ",findMinLoss_iterative(N, A))
print("lrucache: ",find_min_loss(A, N))
print("hashmap: ",findMinLoss_hashmap(N, A))
print("bruteforce : ",findMinLoss_brute_force(N, A)) 


# if __name__ == "__main__":
#     N = int(input().strip())
#     A = list(map(int, input().strip().split()))
#     print(find_min_loss(tuple(A), N))

""" Question
Cold Drink 

There are N cold drinks in a row, with integers denoting the cost of each cold drink respectively.
Each day you can sell the first or the last cold drink in the row.
Initial loss from the cold drinks is A1, A2, A3,..., An.
On the Kth day, the loss from the ith cold drink is K * A[i].
Calculate the minimum loss from all the cold drinks.
 
Function Description
In the provided code snippet, implement the provided findMinLoss(...) method to calculate the minimum loss from all the cold drinks. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”.

There will be multiple test cases running so the Input and Output should match exactly as provided. The base Output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables.

Input Format
The first line contains an integer N, denoting the number of cold drinks.
The second line contains N space-separated integers, denoting the elements of array A.
 
Sample Input

3                 -- denotes N
10 20 30     -- denotes A

Constraints
1 <= N <= 13
1 <= Ai <= 1000

Output Format
The output contains a single integer denoting the minimum loss from all the cold drinks.

Sample Output
100
 
Explanation
On the 1st day, we sell the last cold drink, so the first day's loss is 30 * 1 = 30.
On the 2nd day, we sell the last cold drink, so the second day's loss is 20 * 2 = 40.
On the 3rd day, we sell the last cold drink, so the loss on the third day is 10 * 3 = 30.
The total loss would be 30 + 40 + 30 = 100.
Hence, the output is 100."""