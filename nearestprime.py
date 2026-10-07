import math

def isprime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def b_p(n):
    x = n - 1

    while x >= 2:
        if isprime(x):
            return x
        x -= 1

    return None


def n_p(n):
    x = n + 1

    while True:
        if isprime(x):
            return x
        x += 1


n = int(input())

if n <= 0:
    print()
else:
    bp = b_p(n)
    np = n_p(n)

    if bp is None:
        print(np)
    else:
        bd = n - bp
        nd = np - n

        if nd < bd:
            print(np)
        elif bd < nd:
            print(bp)
        else:
            print(bp, np)





def prime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def b_prime(n):
    x=n-1
    while x>=2:
        if prime(x):
            return True
        x-=1
    return None
def n_prime(n):
    x=n+1
    while True:
        if prime(x):
            return True
        x+=1
n=int(input())
if n<=0:
    print("Invalid Input")
else:
    bp=b_prime(n)
    np=n_prime(n)
    if bp is None:
        print(np)
    else:
        bd=n-bp
        nd=np-n
        if bd<nd:
            print(bp)
        elif nd<nd:
            print(np)
        else:
            print(bp,np)