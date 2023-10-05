arr = [int(v) for v in input().split(" ")]
sum = int(input())
l = len(arr)
csum = arr[0]
low = 0
high = 1
while high <= l:
    while csum > sum and low < high -1 :
        csum -= arr[low]
        low +=1
    if csum == sum:
        print(f"found at [{low},{high-1}]")
        break
    if high < l:
        csum += arr[high]
        high +=1

if csum != sum:
    print("None found")

