# def neon(n):
#     # if n==0:
#     #     return True
#     sqr=n**2
#     sum=0
#     while sqr>0:
#         sum+=sqr%10
#         sqr//=10
#     if sum==n:
#         return True
#     else:
#         return False
# n=int(input("enter the number"))
# if neon(n):
#     print(f"{n} is neon number")
# else:
#     print(f"{n} is not neon number")




def neon(n):
    sqr=n**2
    sum=0
    while sqr>0:
        r=sqr%10
        sum+=r
        sqr//=10
    if sum==n:
        return True
n=int(input())
if neon(n):
    print("neon")
else:
    print("not")
