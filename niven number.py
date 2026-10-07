# def niven_number(n):
#     t=n
#     sum=0
#     while t>0:
#         sum+=t%10
#         t//=10
#     if n%sum==0:
#         return True
#     else:
#         return False
# n=int(input())
# if niven_number(n):
#     print(f"{n} is niven number")
# else:
#     print(f"{n} is not niven number")


def niven(n):
    sum=0
    t=n
    while n>0:
        r=n%10
        sum+=r
        n//=10
    if t%sum==0:
        return True
n=int(input())
if niven(n):
    print("niven")
else:
    print("not")