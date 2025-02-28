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
