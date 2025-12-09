x = input()
print("No") if any(x[i] != x[-(i + 1)] for i in range(int(len(x) / 2))) else print("Yes")