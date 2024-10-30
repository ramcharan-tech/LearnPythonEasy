def selection_sort(arr,debug=False):
    
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j
        if i != min:
            (arr[i],arr[min]) = (arr[min],arr[i])
        if debug:
          print("iterating ",i," for array" , arr)
    return arr

arr = [5,6,4,3,2,1]
print(selection_sort(arr,True))

for i in range(1,1):
    print(i) # doesn't print because 1 is excluded
# selects a minimum elelment
# best and worst case is O(n2)

