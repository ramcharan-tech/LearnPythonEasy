
def bruteforce(arr):
    res = 0

    # For every element of the array
    for i in range(1, len(arr) - 1):

        # Find the maximum element on its left
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])

        # Find the maximum element on its right
        right = arr[i]
        for j in range(i + 1, len(arr)):
            right = max(right, arr[j])

        # Update the maximum water
        res += (min(left, right) - arr[i])

    return res
    
def maxlist(arr):
    n = len(arr)

    # left array
    left = [0] * n
    # right array
    right = [0] * n

    res = 0

    # fill left array
    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], arr[i])

    # fill right array
    right[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], arr[i])

    # calculate the accumulated water element by element
    for i in range(1, n - 1):
        min_of_2 = min(left[i], right[i])
        res += min_of_2 - arr[i]

    return res

def twopointers(arr):
    left = 1
    right = len(arr) - 2

    # lMax : Maximum in subarray arr[0..left-1]
    # rMax : Maximum in subarray arr[right+1..n-1]
    lMax = arr[left - 1]
    rMax = arr[right + 1]

    res = 0
    while left <= right:
      
        # If rMax is smaller, then we can decide the 
        # amount of water for arr[right]
        if rMax <= lMax:
          
            # Add the water for arr[right]
            res += max(0, rMax - arr[right])

            # Update right max
            rMax = max(rMax, arr[right])

            # Update right pointer as we have decided 
            # the amount of water for this
            right -= 1
        else: 
          
            # Add the water for arr[left]
            res += max(0, lMax - arr[left])

            # Update left max
            lMax = max(lMax, arr[left])

            # Update left pointer as we have decided 
            # the amount of water for this
            left += 1
    return res

def trap(height):
    # Edge case: Empty list
    if not height:
        return 0
    
    # Initialize pointers
    left, right = 0, len(height) - 1
    
    # Initialize max heights found so far
    left_max = height[left]
    right_max = height[right]
    
    water_trapped = 0
    
    while left < right:
        # We process the side with the smaller max height
        # because the water level is always limited by the shorter wall.
        if left_max < right_max:
            left += 1
            # Update left_max if current height is taller
            left_max = max(left_max, height[left])
            # Add trapped water (if any)
            water_trapped += left_max - height[left]
        else:
            right -= 1
            # Update right_max if current height is taller
            right_max = max(right_max, height[right])
            # Add trapped water (if any)
            water_trapped += right_max - height[right]
            
    return water_trapped

def using_stack(arr):
    st = []
    res = 0

    for i in range(len(arr)):
       
        # Pop all items smaller than arr[i]
        while st and arr[st[-1]] < arr[i]:
            pop_height = arr[st.pop()]

            if not st:
                break

            # arr[i] is the next greater for the removed item
            # and new stack top is the previous greater 
            distance = i - st[-1] - 1

            # Take the minimum of two heights (next and prev greater)
            water = min(arr[st[-1]], arr[i])

            # Find the amount of water
            water -= pop_height

            res += distance * water
        st.append(i)

    return res

if __name__ == "__main__":
    arr = [2, 1, 5, 3, 1, 0, 4]
    print(bruteforce(arr))
    print(maxlist(arr))
    print(twopointers(arr))
    print(trap(arr))
    print(using_stack(arr))
# Different approaches to trapping rain water problem