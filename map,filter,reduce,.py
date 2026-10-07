l=[[1,2],[3,4],[5,6]]
k=list(map(lambda x:list(map(lambda y:y+5,x)),l))
print(k)

d={"apple":100,"banana":40,"cherry":150}
k=dict(filter(lambda x:x[1]>50,d.items()))
print(k)

from functools import reduce
l=[2,3,4,33,31,44]
largest=reduce(lambda x,y:x if x>y else y,l)
print(largest)

#reduce allows only 2 parameters
l=[1,2,3,4,3,4]
k=reduce(lambda x,y:x+y,l)
print(k)


l="python"
k=list(map(ord,l))
print(k)

s=input()
v="AEIOUaeiou"
k=list(filter(lambda x:x not in v,s))
print(k)

l=["a","b","c","d"]
k=reduce(lambda x,y:x+y,l)
print(k)


l=[1,2,3,4,5,6]
k=list(map(id,l))
print(k)

k=list(map(str,[1,2,3,4,5,6]))#this is better approch faster
l=list(map(lambda x:str(x),[1,2,3,4,5,6]))
print(k)
print(l)


l=[5,10,15,20,25,30]
k=reduce(lambda x,y:x+y,filter(lambda x:x%5==0,map(lambda x:x**2,l)))
print(k)


