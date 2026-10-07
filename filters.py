l=[1,2,3,4,5]
f=list(filter(lambda x:x%2==0,l))
print(f)

s=input()
v="AEIOUaeiou"
k=list(filter(lambda x:x not in v,s))
print(k)

l=[1,2,3,4,5,6,7,8,9,10]
k=list(filter(lambda x:x%3,l))
print(k)



marks=[12,13,16,17,19]
def check(n):
    if n>=15:
        return True
k=list(filter(check,marks))
print(k)
print(list(filter(lambda x:x>=15,marks)))

