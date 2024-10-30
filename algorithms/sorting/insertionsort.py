def insertion_sort_2(arr):

    for i in range(len(arr)-1):
        key = i+1
        for j in range(key,-1,-1):
            print(" j is {}".format(j))
            if arr[j] > arr[key]:
                (arr[j],arr[key])=(arr[key],arr[j])
                key = j
    return arr

def insertion_sort(arr):

    for step in range(1, len(arr)):
        j = step -1
        key = arr[step]

        while j >=0 and key < array[j]:
            array[j+1] =array[j]


arr = [5,6,4,3,2,1]
print(insertion_sort(arr))
# bubbles up highest to last at each sub section iteration 
# , the sub section starts from 0 to 1 and ends ar 0 to n-1
# worst case and best case is O(n2) and O(n)