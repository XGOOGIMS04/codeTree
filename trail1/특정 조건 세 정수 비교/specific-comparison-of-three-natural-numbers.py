a, b, c = map(int, input().split(" "))
# b, c중 작은 값이 a와 같으면 1
if(b < c) and (a == b): # b가 작고 b와 첫번째 수와 일치한다면
    print(1, end=" ") # 1출력
elif (c < b) and (a == c): # c가 작고, c와 첫번째수가 일치한다면
    print(1, end=" ") # 1출력
elif (a <= b) and (a <= c) and (a == a): # a가 젤 작으면
    print(1, end=" ") # 1출력
elif (b < c) and (a != b): # b가 작지만 첫번째 수와 일치하지 않으면
    print(0, end=" ") # 0출력
elif (c < b) and (a != c): # c가 작으나 첫번째수와 일치하지 않는다면
    print(0, end=" ") # 0출력

if(a == b) and (b == c) and (c == a): # 만약 세 수가 모두 같으면
    print(1, end=" ")
else:
    print(0, end=" ")

