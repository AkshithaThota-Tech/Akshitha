
def suny(n):
    n=n+1
    for i in range(1,n+1):
        if i*i==n:
            return True
    return False
n=int(input())
if suny(n):
    print("suny")
else:
    print("not")


