# # #tech Number
# # def tech(n):
# #     n=str(n)
# #     length=len(n)
# #     if length%2==0:
# #         part=length//2
# #         first=n[:part]
# #         last=n[part:]
# #         sum=int(first)+int(last)
# #         sqr=sum**2
# #         if sqr==int(n):
# #             print(f"{n} is tech number")
# #         else:
# #             print(f"{n} is not tech number")
# # n=int(input("enter the number"))
# # tech(n)
#
#
# #tech
# #81-->(8+1)^2=81
# #2025--->(20+25)^2=2025
# #3025--->(30+25)^2=3025
# #9999--->(99+99)^2=39204
# def tech(n):
#     t = n
#     c = 0
#     while n > 0:
#         c += 1
#         n //= 10
#     if c % 2 == 1:
#         return False
#     p = 10 ** (c // 2)  #splitting value
#     a = n // p  #get first value
#     b = n % p  #get second value
#     if (a + b) ** 2 == n:
#         return True
#     else:
#         return False
# n = int(input("enter the number"))
# if tech(n):
#     print(f"{n} is tech number")
# else:
#     print(f"{n} is not tech number")
#
#
# ##atomorphic
# # def ato(n):
# #     sqr=n**2
# #     length=len(str(n))
# #     sqr_str=str(sqr)
# #     last_dig=sqr_str[-length:]
# #     if last_dig==str(n):
# #         print("auto morphic number")
# #     else:
# #         print(f"{n} is not automorphic number")
# # n=int(input("enter the number"))
# # ato(n)
#
#
# #1-->1^2=1
# #5-->5^2=25
# #6-->6^2=36
# #25-->25^2=625
# #76-->76^2=5776
# #using loop
def auto(n):
     sqr = n * n
     while n > 0:
         if sqr % 10 != n % 10:
             return False
         n //= 10
         sqr //= 10
     return True
n = int(input("enter the number"))
if auto(n):
     print(f"{n} is automorphic number")
else:
     print(f"{n} is not automorphic number")
#
#
# # #Strong number
# #1--->1!=1
# #2--->2!=2
# #145--->1!+4!+5!=145
#
# def stng(n):
#     sum = 0
#     t = n
#     while n > 0:
#         r = n % 10
#         f = 1
#         for i in range(1, r + 1):
#             f = f * i
#         sum += f
#         n //= 10
#     if sum == t:
#         return True
# n = int(input("enter the number"))
# if stng(n):
#     print(f"{n} is strong number")
# else:
#     print(f"{n} is not strong number")

#Happy nummber
#1---->1
#19---->1^2+9^2=82----->8^2+2^2=68---->6^2+8^2=100---->1^2+0^2+0^2=1
def hpy(n):
    while n!=1 and n!=4:
        sum=0
        while n>0:
            r=n % 10
            sum+=r*r
            n //= 10
        n=sum
    if n==1:
        return True
    else:
        return False
n=int(input("enter the number"))
if hpy(n):
    print(f"{n} is hpy number")
else:
    print(f"{n} is not hpy number")






#0--->sum=0,product=0
#1--->sum=1,product=1
#22--->sum=4,pro=4
#123--->sum=6,pro=6
#spy number
def spy(n):
    sum = 0
    product = 1
    while n > 0:
        r = n % 10
        sum = sum + r
        product = product * r
        n //= 10
    if sum == product:
        return True
    else:
        return False
n = int(input("enter the number"))
if spy(n):
    print(f"{n} is spy number")
else:
    print(f"{n} is not spy number")



#pronic number
#0=0*1
#2=1*2
#6=2*3
#12=3*4
def pronic(n):
    for i in range(1, n):
        if i * (i + 1) == n:
            return True
n = int(input("enter the number"))
if pronic(n):
    print(f"{n} is pronic number")
else:
    print(f"{n} is not pronic number")


#sunny number
#0---->0+1=1=1^2
#3---->3+1=4=2^2
#8----->8+1=9=3^2
def sunny(n):
    n = n + 1
    for i in range(1, n):
        if i * i == n:
            return True
n = int(input("enter the number"))
if sunny(n):
    print(f"{n} is sunny number")
else:
    print(f"{n} is not sunny number")


#Niven Number
#1---->1%1
#12--->12%3
#18----.18%9
#21---->21%3
def niven(n):
    t = n
    sum = 0
    while n > 0:
        r = n % 10
        sum = sum + r
        n //= 10
    if t % sum == 0:
        return True
    else:
        return False
n = int(input("enter the number"))
if niven(n):
    print(f"{n} is niven number")
else:
    print(f"{n} is not niven number")


#neon Number
#0--->0^2=0
#1---->1^2=1
#9---->9^2=81----->8+1=9
def neon(n):
    sqr = n * n
    sum = 0
    while sqr > 0:
        r = sqr % 10
        sum += r
        sqr //= 10
    if n == sum:
        return True
    else:
        return False
n = int(input("enter the number"))
if neon(n):
    print(f"{n} is neon number")
else:
    print(f"{n} is not neon number")


#Duck
#205,90,101,9022
def Duck(n):
    while n > 0:
        r = n % 10
        if r == 0:
            return True
        n = n // 10
n = int(input("enter the number"))
if Duck(n):
    print(f"{n} is duck number")
else:
    print(f"{n} is not duck number")
