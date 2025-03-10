class Solution: # https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1?page=1&sortBy=submissions
    def subarraySum(self, arr, target):
        
        i,j=0,1
        for k in range(1,len(arr)):
           arr[k] = arr[k-1] + arr[k]
        if target in arr:
            return [1,arr.index(target)+1]
        while j < len(arr):
            currsum = arr[j]-arr[i]
            if currsum < target:
               j+=1
            elif currsum > target:
               i+=1
            else:
               return [i+2,j+1]
            if i==j: j+=1
        return [-1]
    def sumprefixarr(self,arr,target):
        l = len(arr)
        pa = [0]* l
        pa[0] = arr[0]
        for k in range(1,l):
            pa[k] = pa[k-1]+arr[k]
        i,j=0,1
        if target in pa: return [1,pa.index[target]+1]
        while j < l:
            csum = pa[j] - pa[i]
            if csum == target: return [i+2,j+1]
            elif csum > target:i+=1
            else:j+=1
            if i==j:j+=1
        return [-1]
    def sumhashmap(self,arr,target):
        ps, hm= 0, {0:0}
        for i,v in enumerate(arr):
            ps += v
            if ps-target in hm: return [hm[ps-target]+1,i+1]
            hm[ps] = i+1
        return [-1]
            


        





sol = Solution()
tup = ([1, 2, 3, 7, 5],12)
print(sol.sumhashmap(*tup))