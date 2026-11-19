a, b = map(int, input().split())
num1 = a // b
num2 = a % b
print(num1, end=".")
for _ in range(20):
    how = num2 * 10 
    number = how // b
    print(number, end="")
    num2 = how % b
