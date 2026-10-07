import math
def prime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
n=int(input())
p=2
for i in range(1,n+1):
    j=1
    while j<=i:
        if prime(p):
            print(p,end=" ")
            j+=1
        p+=1
    print()



n=int(input())
a,b=0,1
p=2
ct=1
for i in range(1,n+1):
    for j in range(1,i+1):
        if ct%2==1:
            while prime(p)==False:
                p+=1
            print(p,end=" ")
            p+=1
        else:
            print(a,end=" ")
            c=a+b
            a=b
            b=c
        ct+=1
    print()








n=int(input())
a,b=0,1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(a,end=" ")
        c=a+b
        a=b
        b=c
    print()

import math
def prime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
n=int(input())
a,b=0,1
p=2
ct=1
for i in range(1,n+1):
    for j in range(1,i+1):
        if ct%2==1:
            while prime(p)==False:
                p+=1
            print(p,end=" ")
            p+=1
        else:
            print(a,end=" ")
            c=a+b
            a=b
            b=c
        ct+=1
    print()






