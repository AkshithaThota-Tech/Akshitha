lst=[1,2,3,4,5,6,7]
res=list(map(lambda x:x*2,filter(lambda x:x%2==0,lst)))
print(res)

def funcs(lst):
    l=[]
    for i in lst:
        if i%2==0:
            i=i*2
            l.append(i)
    print(l)
def my_map(func,lst):
    func(lst)
my_map(funcs,lst)

# def great(name,prefix='Hello',formatter=lambda)




# student_records=[{'name':'Kenny','score':85},{'name':'harry','score':87},{'name':'joe','score':53},{'namme':'Marcus','score':48},{'name':'clara','score':90}]
# fil=list(filter(lambda x:x["score"]>=60,student_records))
# def grade(x):
#     x['grade']="pass"
#     return x
# grade=list(map(grade,fil))
# print(grade)
# res=sorted(grade,key=lambda x:x['score'],reverse=True)
# print(res)


student_records=[{'name':'Kenny','score':85},{'name':'harry','score':87},{'name':'joe','score':53},{'namme':'Marcus','score':48},{'name':'clara','score':90}]
def grade(x):
    x['grade']="pass"
    return x
res=sorted((map(grade,filter(lambda x:x["score"]>=60,student_records))),key=lambda x:x['score'],reverse=True)
print(res)

student=[("Akshitha",99),("sandhya",95),("Teju",98),("bavani",100)]
s=sorted(student,key=lambda x:x[1],reverse=True)
print(s)

price=[200,330,400,220,810,390,780,970]
filter_prices=list(filter(lambda x:x>500,price))
print(filter_prices)
dis=list(map(lambda x:x-(x*0.1),filter_prices))
print(dis)
import functools
total_price=functools.reduce(lambda x,y:x+y,dis)
print(total_price)



double=lambda x:x*2
triple=lambda x:x*3
quadruple=lambda x:x*4
l=[double,triple,quadruple]
def apply_all(funcs,value):
    for i in funcs:
        value=i(value)
    return value
value=int(input())
print(apply_all(l,value))


logs=["09:15 [INFO] Server started","13;42 [ERROR] Disk full","11:50 [ERROR] Timeout","15:03 [INFO] Request OK","14:20 [ERROR] DB connection lost"]
error=list(filter(lambda x:"[ERROR]" in x,logs))
print(error)


# def create_password(password):
#     def check_password(password):
#         if create_password==check_password:
#             print("Access Granted")
#         else:
#             print("Access Denied")
#     return check_password
#
# print(create_password("akshi12"))



l=[1,2,3,4,5,6,7]
# even=list(filter(lambda x:x%2,l))
multi=list(map(lambda x:x*2,(filter(lambda x:x%2==0,l))))
print(multi)


def fun(l):
    lst=[]
    for i in l:
        if i%2==0:
            i=i*2
            lst.append(i)
    return lst
def my_map(func,l):
    func(l)
my_map(func,l)


l=student=[("Akshitha",99),("sandhya",95),("Teju",98),("bavani",100)]
res=sorted(l,key=lambda x:x[1],reverse=True)
print(res)


student_records=[{'name':'Kenny','score':85},{'name':'harry','score':87},{'name':'joe','score':53},{'name':'Marcus','score':48},{'name':'clara','score':90}]
# fil=list(filter(lambda x:x['score']>=60,student_records))
# print(fil)
def grade(x):
    x['grade']="pass"
    return x
# grade=list(map(grade,(filter(lambda x:x['score']>=60,student_records))))
des=sorted((map(grade,(filter(lambda x:x['score']>=60,student_records)))),key=lambda x:x['score'],reverse=True)
print(des)



lst=[200,500,600,700,800]
fil=list(filter(lambda x:x>500,lst))
m=list(map(lambda x:x-x*0.1,fil))
import functools
total_price=functools.reduce(lambda x,y:x+y,m)
print(total_price)


