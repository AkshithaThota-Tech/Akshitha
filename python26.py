def display_message():
    print("Python is easy to learn")
display_message()

def welcome(name):
    print(f"Welcome {name}")
welcome("AKshi")

def cube(n):
    return n*n*n
print(cube(5))

def is_even(n):
    return n % 2 == 0
print(is_even(3))

def full_name(first,last):
    return f"{first}{last}"
print(full_name("AKshi","thota"))

def area_of_rectangle(length,width):
    return length*width
print(area_of_rectangle(4,5))

def add(a,b):
    return a+b
print(add(3,4))




import copy

a=[[1,2,3],[4,5,6],[7,8,9]]
shallow=copy.copy(a)
deepcopy=copy.deepcopy(a)
a[0].append(10)
a.append(20)
print(a)
print(shallow)#access modified inner list only
print(deepcopy)#didn't access both inner and outer modified list



def calculate_total(price,tax=5,discount=0):
    return price+tax-discount
print(calculate_total(100))
print(calculate_total(100,100))
print(calculate_total(100,10,10))
print(calculate_total(100,100,10))



def create_profile(name,*skills,**details):
    print("Name:",name)

    print("Skills:")
    for skill in skills:
        print("-",skill)
    print("Details:")
    for i,j in details.items():
        print(i,j)
create_profile("Akshi","python","sql","DSA",grade="A",rollno="21")


def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
operation={1:addition,2:subtraction,3:multiplication}
for i,j in operation.items():
    print(f"{i}")
user_choice=int(input("Enter your choice:"))
a=int(input("Enter a:"))
b=int(input("Enter b:"))
if user_choice in operation:
    res=operation[user_choice](a,b)
    print(res)
else:
    print("Invalid Choice")

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
d={1:add,2:sub,3:mul}
for i,j in d.items():
    print(i)
user=int(input())
a=int(input())
b=int(input())
if user in d:
    res=d[user](a,b)
    print(res)
else:
    print("Invalid Input")

    