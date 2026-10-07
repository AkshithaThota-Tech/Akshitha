# def spy(n):
#     sum=0
#     prod=1
#     if n==0:
#         return True
#     while n>0:
#         r=n%10
#         sum+=r
#         prod*=r
#         n//=10
#     if prod==sum:
#         return True
#     else:
#         return False
# n=int(input("enter the number"))
# if spy(n):
#     print(f"{n} is spy number")
# else:
#     print(f"{n} is not spy number")


def spy(n):
    s=0
    p=1
    if n==0:
        print("spy")
    else:
        while n>0:
            r=n%10
            s+=r
            p*=r
            n//=10
        if p==s:
            print("spy")
        else:
            print("no")
n=int(input())
spy(n)