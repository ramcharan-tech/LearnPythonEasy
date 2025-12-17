# if positive extend else restart --> kadanes algorithm
def maxsubarray(arr):
    currmax = arr[0]
    res = arr[0]
    currstart = 0
    resstart = 0
    resend = 0
    for i in range(1, len(arr)):
        if arr[i] > currmax + arr[i]:
            currmax = arr[i]
            currstart = i
        else:
            currmax += arr[i]
        
        if currmax > res:
            res = currmax
            resstart = currstart
            resend = i
    return arr[resstart:resend+1]

def maxsubarray_sum(arr):
    currmax = arr[0]
    res = arr[0]
    for i in range(1, len(arr)):
        if currmax < 0:
            currmax = arr[i]
        else:
            currmax += arr[i]
        res = max(res, currmax)
    return res

def maxsubarray_sum_recursive(arr):
    def helper(i):
        if i == 0:
            return arr[0], arr[0]
        prev_max_end, overall_max = helper(i - 1)
        curr_max_end = max(arr[i], prev_max_end + arr[i])
        overall_max = max(overall_max, curr_max_end)
        return curr_max_end, overall_max

    _, res = helper(len(arr) - 1)

def maxsubarray_sum_memo(arr):
    memo = {}

    def helper(i):
        if i in memo:
            return memo[i]
        if i == 0:
            memo[i] = (arr[0], arr[0])
            return memo[i]
        prev_max_end, overall_max = helper(i - 1)
        curr_max_end = max(arr[i], prev_max_end + arr[i])
        overall_max = max(overall_max, curr_max_end)
        memo[i] = (curr_max_end, overall_max)
        return memo[i]

    _, res = helper(len(arr) - 1)

def maxsubarray_sum_dp(arr):
    n = len(arr)
    dp = [0] * n
    dp[0] = arr[0]
    res = arr[0]
    for i in range(1, n):
        dp[i] = max(arr[i], dp[i - 1] + arr[i])
        res = max(res, dp[i])



def maxsubarray_sum_kadane(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]
    
    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

if __name__=="__main__":
    
    arr =[ 2, 3, -8, 7, -1, 2, 3]
    
    print(maxsubarray_sum(arr))