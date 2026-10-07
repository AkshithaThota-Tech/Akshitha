# def hpy(n):
#     while n!=1 and n!=4:
#         sum=0
#         while n>0:
#             r=n%10
#             sum+=r*r
#             n//=10
#         n=sum
#     if n==1:
#         return True
#     else:
#         return False
# n=int(input("enter the number"))
# if hpy(n):
#     print(f"{n} is hpy number")
# else:
#     print(f"{n} is not hpy number")


def hpy(n):
    while n!=1 and n!=4:
        sum=0
        while n>0:
            r=n%10
            sum+=r*r
            n//=10
        n=sum
    if n==1:
        return True
    else:
        return False
n=int(input())
if hpy(n):
    print("hpy")
else:
    print("not")
