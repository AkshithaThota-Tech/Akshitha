# 1. Create a decorator that prints a message before and after executing a function.
# 	Expected output:
# 	Before function execution
# 	Hello Student
# 	After function execution



def decorator(func):
    def inner():
        print("Before Function execution")
        func()
        print("After Function execution")
    return inner
@decorator
def greet():
    print("Hello Student")
greet()



#
# 2. Create a decorator my_decorator for the below function:
# 	def greet():
#     		print("Good Morning")
# Output should be:
# Welcome Message
# Good Morning
# Thank You Message

def my_decorator(func):
    def inner():
        print("Welcome Message")
        func()
        print("Thank You")
    return inner
@my_decorator
def greet():
    print("Good Morning")
greet()

# 3. Create a decorator that accepts a function with parameters.
# Example:
# @calculate
# def add(a,b):
#     print(a+b)
#
# add(10,20)
# Output:
# Addition result: 30

def calculate(func):
    def inner(a,b):
        func(a,b)
    return inner
@calculate
def add(a,b):
    print(a+b)
add(10,10)



# 4. Create a decorator to check whether a number is even or odd before executing a function.
# Example:
# @check_number
# def show(n):
#     print("Number accepted")
# Input:
# show(10)
# Output:
# Even number
# Number accepted


def check_number(func):
    def inner(n):
        if n%2==0:
            print("Even Number")
        else:
            print("Odd number")
        func(n)
    return inner
@check_number
def show(n):
    print("Number accepted")
show(10)




# 5. Create a login verification decorator.
# Requirement:
# If user is logged in:
# 	Access granted
# 	Welcome to profile
# Otherwise:
# 	Please login first
# Example:
# @login_required
# def profile():
#     print("Welcome to profile")
def login_required(func):
    def check(logged_in):
        if logged_in:
            print("Access granted")
            func()
        else:
            print("Please Login")
    return check
@login_required
def profile():
    print("Welcome to profile")
profile(True)



def password_validator(func):
    def Wrapper(password):
        if len(password)<=8:
            print("Invalid Password")
            return

        capital=False
        small=False
        special=False
        number=False

        for ch in password:
            if ch.isupper():
                capital=True
            elif ch.islower():
                small=True
            elif ch.isdigit():
                number=True
            else:
                special=True
        if capital and small and number and special:
            print("Valid Password")
            func(password)
        else:
            print("Invalid password")
    return Wrapper
@password_validator
def login(password):
    print("password accepted")
login("Akshi@123")





count=0

def validate_positive(func):
    def Wrapper(*args):
        global count
        count+=1
        print(f"function is called count={count}")
        for i in args:
            if i<0:
                print("Error:Negative Value")
                return None
            return func(*args)
    return Wrapper
@validate_positive
def check(a,b):
    print(a+b)
check(10,20)
check(-10,20)



def logger(func):
    def wrapper(name):
        print("function started")
        func(name)
        print("function ended")
    return wrapper
def repeat(n):
    def decorator(func):
        def wrapper(name):
            for i in range(n):
                func(name)
        return wrapper
    return decorator
@repeat(3)
@logger
def great(name):
    print("Hello",name)
greet("Akshitha")




























