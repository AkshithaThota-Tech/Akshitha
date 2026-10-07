x=200
def outer():
    def inner():
        print("hello")
    x=300
    print(x)
    inner()
outer()

def greet():
    print("hello")
    def say_hello():
        print("Bye")
    say_hello()
greet()



def calc(x,y):
    def add(a,b):
        print(a+b)
    def mul(a,b):
        print(a*b)
    add(x,y)
    mul(x,y)
a=int(input())
b=int(input())
calc(a,b)


def exam(name,age):
    print("Exam Started")
    def submit():
        print("Name",name)
        print("Age",age)
        print('Exams Submitted')
    submit()
name=input()
age=int(input())
exam(name,age)

#(OR)

def exam(name,age):
    def submit():
        print("Name",name)
        print("Age",age)
        print('Exams Submitted')
    print("Exam Started")
    submit()
name=input()
age=int(input())
exam(name,age)


import math
a=100
def fun():
    x=300
    def fun2():
        y=200
        print(y,x,a,math.pi)
    fun2()
fun()



x=500
def fun():
    global x
    x=300
print(x)
fun()
print(x)


x=500
def fun():
    a=100
    def fun2():
        a=700
        global x
        x=200
    print(a,x)
    fun2()
    print(a,x)
fun()


x=500
def fun():
    a=100
    def fun2():
        nonlocal a
        a=700
        global x
        x=200
    print(a,x)
    fun2()
    print(a,x)
fun()


def fun():
    a=100
    def fun2():
        nonlocal a
        a=700
    print(a)
    fun2()
    print(a)
fun()


def fun():
    a=150
    def fun2():
        nonlocal a
        def fun3():
            nonlocal a
            a=700
        fun3()
    fun2()
fun()


def calc(a,b,op):
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    if op=="+":
        return add(a,b)
    elif op=="-":
        return sub(a,b)
    else:
        return mul(a,b)
print(calc(10,20,"+"))




