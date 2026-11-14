per1_age, per1_sex = input().split()
per1_age = int(per1_age)
per2_age, per2_sex = input().split()
per2_age = int(per2_age)

if(per1_age >= 19 and (per1_sex == "M")) or (per2_age >= 19 and (per2_sex == "M")):
    print(1)
else:
    print(0)