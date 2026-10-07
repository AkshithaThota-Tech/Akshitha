def greet(name):
    print(f"Hello {name}")
welcome=greet
welcome("Akshitha")



def square(n):
    return n*n
s=square
print(s(6))


def message():
    print("Hello Python")
m=message
m()
m()
m()

l=[1,2,3,4]
count=len
print(count(l))


display=print
display("Functional Reference")


def cube(n):
    return n*n*n
def apply(func,value):
    return func(value)
print(apply(cube,3))



def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def calculate(operation,a,b):
    return operation(a,b)
print(calculate(add,2,3))
print(calculate(sub,9,4))


def is_even(num):
    return num%2==0
def check(func,num):
    return func(num)
print(check(is_even,10))

