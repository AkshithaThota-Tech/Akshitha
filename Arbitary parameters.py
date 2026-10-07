def values(*args):
#     for i in args:
        print(args)
values(1,2,3,4,5)



def product(*args):
    p=1
    for i in args:
        p=p*i
    print(p)
product(1,2,3,4,5)



def count(*args):
    c=0
    for i in args:
        c+=1
    return c
print(count(1,2,3,4,5))

#0r
def count(*args):
    print(len(args))
count(1,2,3,4,5)



def even(*args):
    res=[]
    for i in args:
        if i%2==0:
            res.append(i)
    print(res)
even(1,2,3,4,5)


def types(*args):
    for i in args:
        print(type(i))
types(1,2,3,"Hello",2.2,True)


def stu_details(**details):
    print("Details:")
    for i,j in details.items():
        print(f"{i}: {j}")
stu_details(name="Akshi",age=22,city="siddipet",vlg="Kurella")



def count(**kwargs):
    c=0
    for i,j in kwargs.items():
        c+=1
    print(c)
count(name="Akshi",age=22,city="siddipet",vlg="Kurella")



def keys(**kwargs):
    for i in kwargs.keys():
        print(i)
keys(name="Akshi",age=22,city="siddipet",vlg="Kurella")

def value(**kwargs):
    for i in kwargs.values():
        print(i)
value(name="Akshi",age=22,city="siddipet",vlg="Kurella")


