num = int(input())
sq = 0
for i in range(1,num):
    if num == i* i and num/2>i:
        sq = i
        print(sq,"is the square root of",num)
        break
if sq == 0 :
    print("No square root found")