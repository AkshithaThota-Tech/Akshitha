n=int(input())
n1=int(input())
if n<n1:
    c=0
    for i in range(n,n1+1):
        i=i*5
        c+=1
        if i>=0:
            if c>1:
                print(",",end=" ")
            print(i,end="")
        else:
            if c>1:
                print(",",end=" ")
            print(f"({i})",end="")
else:
    c=0
    for i in range(n,n1-1,-1):
        i=i*5
        c+=1
        if i>=0:
            if c>1:
                print(",",end=" ")
            print(i,end="")
        else:
            if c>1:
                print(",",end=" ")
            print(f"({i})",end="")