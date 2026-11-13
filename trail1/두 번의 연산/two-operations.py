A = int(input())
if (A % 2 != 0):
    num = A + 3 
    if(num % 3 == 0):
        print(num // 3)
    if(num % 3 != 0):
        print(num)
if(A % 2 == 0):
    if(A % 3 == 0):
        print(A // 3)
    if(A % 3 != 0):
        print(A)
