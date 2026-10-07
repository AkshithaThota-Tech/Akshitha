from functools import reduce
l=[1,2,3,4,5,6,7,8,9]
k=reduce(lambda x,y:x*y,l)
print(k)

k=["Hi","This","is","a","test"]
st=reduce(lambda x,y:x+" "+y,k)
print(k)

k=["Hello","Hii","who","sentence","bye"]
st=reduce(lambda x,y:x if len(x)>len(y) else y,k)
print(st)

#using initial value
k=[1,2,3,4]
st=reduce(lambda x,y:x*y,k,10)
print(st)

funds=[10,20,30]
def total(a,b):
    return a+b
print(reduce(total,funds))

#default value or initial value
l=[1,2,3,4,5,6]
print(reduce(lambda x,y:x+y,l,30))



