a, b, c = map(int, input().split())
if(a >= b and a >= c): # a가 가장 클때
    print(a)
else:
    if(b >= a and b >= c):
        print(b)
    else:
        print(c)