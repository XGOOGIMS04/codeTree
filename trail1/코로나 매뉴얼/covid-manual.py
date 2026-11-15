per1, per11 = input().split()
per2, per22 = input().split()
per3, per33 = input().split()
per11 = int(per11)
per22 = int(per22)
per33 = int(per33)
n = 0

if(per1 == "Y"):
    if(per11 >= 37):
        n += 1

if(per2 == "Y"):
    if(per22 >= 37):
        n += 1
        
if(per3 == "Y"):
    if(per33 >= 37):
        n += 1

if(n >= 2):
    print("E")
else:
    print("N")