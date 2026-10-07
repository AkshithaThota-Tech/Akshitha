import math
def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
n=int(input("enter the number"))
d=1
while True:
    if isprime(n-d):
        print(n-d)
        break
    elif isprime(n+d):
        print(n+d)
        break
    d+=1


n=int(input("enter the number"))
c=0
num=2
while c<n:
    if isprime(num):
        print(num,end="")
        c+=1
    num+=1

n=int(input("enter the number"))
c=0
num=2
while c<n:
    if isprime(num):
        c+=1
    if c==n:
        print(num,end="")
        break
    num += 1