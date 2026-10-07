#WAP to print Squares of a number
l=[7,6,2,5,8]
def sqr(x):
    return x*x
# e=[]
# for i in l:
#     a=sqr(i)
#     e.append(a)
# print(e)
res=list(map(sqr,l))
print(res)

k=list(map(lambda x:x**2,l))
print(k)



#WAP to convert even to odd
l=[7,6,2,5,8]
def odd(n):
    if n%2==0:
        n+=1
    return n
res=list(map(odd,l))
print(res)

k=list(map(lambda n:n+1 if n%2==0 else n,l))
print(k)

#WAP to convert string into integer
st=["2","3","91","4"]
l=list(map(int,st))
print(l)

#write a program to split a sentence into integer
st="iam akshi from siddipet"
print(st.split("a"))



l=[11,22,32,24,25]
# k=list(map(chr,l))
k=list(map(str,l))
print(k)

l=[1,2,3,4]
l2=[2,3,4,5]
k=list(map(lambda x,y:x+y,l,l2))
print(k)

l1=[1,2,3,4]
l2=[3,4,5,5]
l3=[2,3,4,5]
k=list(map(lambda x,y,z:x+y+z,l1,l2,l3))
print(k)

s="ABCD"
s1="Hello"
s2="Who"
s3=list(map(lambda x,y,z:x+y+z,s,s1,s2))
print(s3)


l1=[1,2,3]
l2=[3,4,5]
k=map(lambda x,y:x+y,l1,l2)
print(k)
print(list(k))
print(tuple(k))
print(set(k))


sal=[12,15,27,33]
def incrmt(n):
    return n+5
print(list(map(incrmt,sal)))
print(list(map(lambda x:x+5,sal)))#use when u didnt want to use again

l=['r','e','d']
k=list(map(ord,l))
print(k)





