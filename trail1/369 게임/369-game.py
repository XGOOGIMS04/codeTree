n = int(input())
for i in range(1, n+1):
    a = str(i)
    if "3" in a or "6" in a or "9" in a or (i % 3 == 0):
        print(0, end=" ")
    else:
        print(i, end=" ")
