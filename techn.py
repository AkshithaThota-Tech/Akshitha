# def tech(n):
#     c=0
#     t=n
#     while n>0:
#         r=n%10
#         c+=1
#         n//=10
#     p=10**(c//2)
#     a=t//p
#     b=t%p
#     if (a+b)**2==t:
#         return True
#     else:
#         return False
# n=int(input("enter number"))
# if tech(n):
#     print(f"{n} is tech number")
# else:
#     print(f"{n} is not tech number")






def tech(n):
    t=n
    c=0
    while n>0:
        r=n%10
        c+=1
        n//=10
    if c%2==1:
        return False
    p=10**(c//2)
    a=n//p
    b=n%p
    if (a+b)**2==t:
        return True
    else:
        return False
n=int(input())
if tech(n):
    print("tech")
else:
    print("not")

