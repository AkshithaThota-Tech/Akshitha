def duck(n):
    while n>0:
        if n%10==0:
            return True
        n//=10
n=int(input("enter the number"))
if duck(n):
    print(f"{n} is duck")
else:
    print(f"{n} not duck")
