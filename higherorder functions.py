l=[1,2,3,4,5]
k=list(map(lambda x:x+5,l))
print(k)

l=[1,2,3,4,5]
sqr=list(map(lambda x:x**2,l))
print(sqr)

l=[1,2,3,4,5]
cube=list(map(lambda x:x**3,l))
print(cube)

l=[1,2,3,4,5]
str=list(map(str,l))
print(str)


l=["hello","hi","nice","world"]
c=list(map(lambda x:len(x),l))
print(c)


cel=[1,2,3,4,5]
f=list(map(lambda c: (c*9/5)+32,cel))
print(f)


l=[1,2,3,4,5]
eo=list(map(lambda x:"even" if x%2==0 else "odd",l))
print(eo)

l=[1,2,3,4,5]
even=list(filter(lambda x:x%2==0,l))
print(even)

l=[1,2,3,4,5]
odd=list(filter(lambda x:x%2,l))
print(odd)

l=[1,20,4,33,3,24,10]
k=list(filter(lambda x:x>10,l))
print(k)

l=["Hello","hii","nice","world"]
k=list(filter(lambda x:len(x)>4,l))
print(k)


l=[3,33,25,65,3,10]
k=list(filter(lambda x:x%5==0,l))
print(k)


l=input()
x="AEIOUaeiou"
k=list(filter(lambda ch:ch in x,l))
print(k)

l=[1,-3,2,-3,2]
k=list(filter(lambda x:x>0,l))
print(k)


l=[1,3,5,2,5,7,8]
eo=list(map(lambda x:"even" if x%2==0 else "odd",l))
print(eo)


l=[1,2,3,4,5,6,7,8,9]
even=list(filter(lambda x:x%2==0,l))
print(even)

l=[1,2,3,4,5,6,7,8,9]
even=list(filter(lambda x:x%2,l))
print(even)


l=[1,22,32,43,5,6,7,8,93]
greater=list(filter(lambda x:x>10,l))
print(greater)


l=["sd","sdfg","rtyuhsdf","assdfghjkl"]
res=list(filter(lambda x:len(x)>4,l))
print(res)

l=[1,2,3,4,5,6,7,8,9]
even=list(filter(lambda x:x%5==0,l))
print(even)




