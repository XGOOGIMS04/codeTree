a = int(input())
if(a % 2 == 0): # 짝수일 경우
    even = a // 2 # even에 2 나눈 수 저장
    if(even % 2 == 0): # 경우1_even 이 짝수면
        print(even) # 그대로 출력
    if(even % 2 != 0): # 경우2_ even 이 홀수이면
        print((even + 1) // 2) # 계산 과정 거친 후 출력
if(a % 2 != 0): # 홀수일 경우
    print((a + 1) // 2)
