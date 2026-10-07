fun1=lambda x,y:x+y
fun2=lambda x:x*2
print(fun1(10,20))
print(fun2(5))
print((lambda x,y:x+y)(10,20))
k=lambda x,y: x if x>y else y
print(k(10,20))

double=lambda x:x*2
triple=lambda x:x*3
square=lambda x:x**2
l=[double,triple,square]
print(l[2](20))
print(l[1](10))
s=20
for i in l:
    s=i(s)
print(s)


def fun():
    print("hello")
x=fun
x()
fun()
def fun2(y):
    y()
fun2(fun)


def fun():
    def fun2():
        print("Hello")
    return fun2
def fun3(y):
    y()
def fun4():
    print("hello")
fun3(fun4)

l=lambda x,y:(x+y)*(x-y)
k=lambda z,a:z*a
print(lambda x,y:x+y)
print(k,l)
def fun(l,x,y):
    print(l(x,y))
fun(l,23,24)
fun(k,15,20)



l=lambda x,y:(x+y)*(x-y)
k=lambda z,a:z*a
li=[lambda x,y:x+y,k,l]

def fun2(s,x,y):
    for i in s:
        print(i(x,y))
fun2(li,7,6)



l=[1,2,3,4,5,6]
n=lambda x:x*x
def mapping(sq,li):
    el=[]
    for i in li:
        s=sq(i)
        el.append(s)
    return el
r=mapping(n,l)
print(r)






