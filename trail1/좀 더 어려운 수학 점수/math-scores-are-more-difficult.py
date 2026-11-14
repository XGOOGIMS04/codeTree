a_math, a_eng = map(int, input().split())
b_math, b_eng = map(int, input().split())

if(a_math == b_math) and (a_eng > b_eng): # 수학점수 같고, a의 영여 점수가 높으면
    print("A") # A 출력
elif(a_math == b_math) and (a_eng < b_eng): # 수학점수 같고, b의 영어 점수 높으면
    print("B") # B 출력
elif(a_math > b_math):
    print("A")
elif(a_math < b_math):
    print("B")