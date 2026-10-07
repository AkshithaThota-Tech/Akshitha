# n=abs(int(input()))
# res=1
# c=0
# for i in range(1,n+1):
#     c+=1
#     if i%3==0:
#         if c>1:
#             print(",",end="")
#         print("@",end="")
#     elif i%3==1:
#         if c>1:
#             print(",",end="")
#         print(1,end="")
#     else:
#         if c>1:
#             print(",",end="")
#         print("A",end="")


#
# s=int(input())
# e=int(input())
# c=0
# for i in range(s,e+1):
#     if i%2==0:
#         c+=1
#         if c%2==1:
#             if c>1:
#                 print(",",end="")
#             print(i,end="")


import math
# def isprime(n):
#     if n<=1:
#         return False
#     for i in range(2,int(math.sqrt(n))+1):
#         if n%i==0:
#             return False
#     return True
# n=int(input())
# d=1
# while True:
#     if isprime(n-d):
#         print(n-d)
#         break
#     elif isprime(n+d):
#         print(n+d)
#         break
#     d+=1


#
# import math
# def isprime(n):
#     if n<=1:
#         return False
#     for i in range(2,int(math.sqrt(n))+1):
#         if n%i==0:
#             return False
#     return True
# def bef_prime(n):
#     x=n-1
#     while True:
#         if isprime(x):
#             return x
#         x-=1
# def nxt_prime(n):
#     x=n+1
#     while True:
#         if isprime(x):
#             return x
#         x+=1
# n=int(input())
# if n<=0:
#     print("Invalid Input")
# else:
#     bp=bef_prime(n)
#     np=nxt_prime(n)
#     bd=n-bp
#     nd=np-n
#     if nd<bd:
#         print(np)
#     elif nd>bd:
#         print(bp)
#     else:
#         print(bp,np)


import math
def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def b_p(n):
    x=n-1
    while x>=2:
        if isprime(x):
            return x
        x-=1
def n_p(n):
    x=n+1
    while True:
        if isprime(x):
            return x
        x+=1
n=int(input())
if n<=0:
    print()
else:
    bp=b_p(n)
    np=n_p(n)
    bd=n-bp
    nd=np-n
    if nd<bd:
        print(np)
    elif bd<nd:
        print(bp)
    else:
        print(np,bp)















# 1,A,@,1,A,@,1,A,@
# 1,2,3,4,5,6,7,8,9