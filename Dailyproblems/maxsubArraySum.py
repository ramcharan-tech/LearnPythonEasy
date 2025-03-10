class Solution:
    def maxSubArraySum(self, arr):
        i,j,l = 0,1,len(arr)
        ps = [0]*l
        ps[0]= arr[0]
        for k in range(1,l):
            ps[k]=ps[k-1]+arr[k]
        max_sum = max(ps)
        while j<l:
            max_sum = max(max_sum,ps[j]-ps[i])
            if ps[j] < ps[i]:
                i = j
                j = i+1
            else:
                j+=1

        return max_sum
    def kadanesalgo(self,arr):
        csum,max_sum = 0,float('-inf')
        for n in arr:
            csum+=n
            max_sum = max(max_sum,csum)
            if csum < 0: csum=0
        return max_sum

sol = Solution()
tup = [-35, 2, 9, -10, 11]
print(sol.kadanesalgo(tup))