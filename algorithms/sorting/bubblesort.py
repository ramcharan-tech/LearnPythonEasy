def bubble_sort(arr,debug=False):
    
    for i in range(len(arr)):
        swap = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swap = True
        if not swap:
            break
        if debug:
          print("iterating ",i," for array" , arr)
    return arr

arr = [1,2,3,4,6,5]
print(bubble_sort(arr,True))
# bubbles up highest number to last at each iteration
# worst case and best case is O(n2) and O(n)

