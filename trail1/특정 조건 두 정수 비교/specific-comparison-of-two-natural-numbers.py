A, B = map(int, input().split(" "))
if(A < B):
    print(1, end=" ")
else:
    print(0, end=" ")
if(A == B):
    print(1, end=" ")
else:
    print(0, end=" ")

#두개의 출력문을 연달아 출력하는 방법 : end=" "