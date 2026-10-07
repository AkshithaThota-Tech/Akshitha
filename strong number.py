# def stng(n):
#     t=n
#     sum=0
#     while n>0:
#         r=n%10
#         f=1
#         for i in range(1,r+1):
#             f=f*i
#         sum+=f
#         n=n//10
#     if sum==t:
#         return True
#     else:
#         return False
# n=int(input("enter the number"))
# if stng(n):
#     print(f"{n} is strong number")
# else:
#     print(f"{n} is not strong number")




def strong(n):
    t=n
    sum=0
    while n>0:
        r=n%10
        f=1
        for i in range(1,r+1):
            f=f*i
        sum+=f
        n//=10
    if sum==t:
        return True
n=int(input())
if strong(n):
    print("strong")
else:
    print("not")



