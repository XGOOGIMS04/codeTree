a, b, c = map(int, input().split())

#a가 중앙값인 경우
if((b >= a) and (a >= c)) or ((b <= a) and (a <= c)):
    print(a)
#b가 중앙값인 경우
if((a <= b) and (c >= b)) or ((a >= b) and (c <= b)):
    print(b)
#c가 중앙값인 경우
if((a <= c) and (b >= c)) or ((a >= c) and (b <= c)):
    print(c)