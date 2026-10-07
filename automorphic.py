# def auto(n):
#     sqr=n*n
#     while n>0:
#         if sqr%10!=n%10:
#             return False
#         sqr//=10
#         n//=10
#     return True
# n=int(input())
# if auto(n):
#     print(f"{n} is auto number")
# else:
#     print(f"{n} is not auto number")
#




def auto(n):
    sqr=n*n
    while n>0:
        if sqr%10!=n%10:
            return False
        n//=10
        sqr//=10
    return True
n=int(input())
if auto(n):
    print("auto")
else:
    print("not")



