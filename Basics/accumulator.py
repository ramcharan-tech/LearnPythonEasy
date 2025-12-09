
def getAlternates(arr, idx=0):
    if idx == 0:
        getAlternates.res = []  # initialize per top-level call
    if idx >= len(arr):
        return
    getAlternates.res.append(arr[idx])
    getAlternates(arr, idx + 2)

# Usage
getAlternates([10, 20, 30, 40, 50])
print(getAlternates.res)  # [10, 30, 50]

getAlternates([1, 2, 3, 4])
print(getAlternates.res)  # [1, 3]