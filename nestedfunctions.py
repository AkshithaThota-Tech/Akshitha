# 1. Basic Nested Function
#
# Create a function outer() and define another function inner() inside it.
#
# - outer() should print "Outer function started".
# - inner() should print "Inner function executed".
# - Call inner() from inside outer().
# - Finally, call outer().


def outer():
    print("Outer function started")
    def inner():
        print("Inner function Started")
    inner()
outer()



# 2. Greeting Example
#
# Create a function called greeting().
#
# Inside it, create another function called say_hello().
#
# - greeting() should print "Welcome!".
# - say_hello() should print "Hello, Student!".
# - Call the inner function from the outer function.


def greeting():
    print("welcome")
    def say_hello():
        print("Hello Student!")
    say_hello()
greeting()



# 3. Passing a Value
#
# Create an outer function called calculate() that accepts a number.
#
# Inside it, define a function square() that calculates and prints the square of that number.
#
# Example:
# Input: 5
# Output: 25

def calculate(n):
    def square():
        print(n**2)
    square()
calculate(5)

# 4. Two Numbers
#
# Create a function operations(a, b).
#
# Inside this function, create another function called add() that prints the sum of a and b.
#
# Example:
# Input: 10, 20
# Output: 30

def operation(a,b):
    def add():
        print(a+b)
    add()
operation(2,4)



# 5. Inner Function with Its Own Parameter
#
# Create an outer function called message().
#
# Inside it, define an inner function display(name).
#
# The inner function should print:
#
# Hello <name>
#
# Call the inner function with a student's name.

def message():
    def display(name):
        print(f"Hello {name}")
    display("AKshi")
message()


# 6. Multiple Inner Functions
#
# Create a function called calculator(a, b).
#
# Inside it, create two functions:
#
# - addition() -> prints the sum
# - multiplication() -> prints the multiplication result
#
# Call both functions from inside calculator().

def calculator(a,b):
    def add():
        print(a+b)
    def mul():
        print(a*b)
    add()
    mul()
calculator(2,3)



# 7. Understanding Scope
#
# Create an outer function that contains a variable:
#
# message = "Python"
#
# Inside the outer function, create an inner function that prints the message variable.
#
# Answer the following:
#
# - Can the inner function access the variable created in the outer function?
# - Write a program to verify your answer.


def outer():
    message="pythonn"
    def inner():
        print(message)
    inner()
outer()

# 8. Return Value from an Inner Function
#
# Create an outer function called calculate().
#
# Inside it, create an inner function called add(a, b) that returns the sum of two numbers.
#
# The outer function should receive the returned value and print it.


def calculate():
    def add(a,b):
        return a+b
    print(add(2,3))
calculate()


# 9. Find Even or Odd
#
# Create a function check_number(number).
#
# Inside it, define a function check() that determines whether the given number is even or odd.
#
# Call the inner function from the outer function.

def check_number(number):
    def check():
        if number%2==0:
            print("even")
        else:
            print("Odd")
    check()
check_number(10)



# 10. Simple Student Example
#
# Create a function called student_details(name).
#
# Inside it, create another function called display().
#
# The inner function should print:
#
# Student Name: <name>
#
# Call display() from inside student_details().

def student_details(name):
    def display():
        print(name)
    display()
student_details("Akshi")

