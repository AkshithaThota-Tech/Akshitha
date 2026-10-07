# def pronic(n):
#     for i in range(0,n):
#         if i*(i+1)==n:
#             return True
# n=int(input())
# if pronic(n):
#     print(f"{n} is pronic number")
# else:
#     print(f"{n} is not pronic number")



def pronic(n):
    for i in range(0,n+1):
        if i*(i+1)==n:
            return True
    return False
n=int(input())
if pronic(n):
    print("pronic")
else:
    print("not")













