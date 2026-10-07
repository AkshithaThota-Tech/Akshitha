
import math
def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def bef_prime(n):
    x=n-1
    while True:
        if isprime(x):
            return x
        x-=1
def nxt_prime(n):
    x=n+1
    while True:
        if isprime(x):
            return x
            x+=1
n=int(input())
if n<=0:
    print("Invalid Input")
else:
    bp=bef_prime(n)
    np=nxt_prime(n)
    bd=n-bp
    nd=np-n
    if nd<bd:
        print(np)
    elif bd<nd:
        print(bp)
    else:
        print(np,bp)