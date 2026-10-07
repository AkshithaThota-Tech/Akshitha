# Question 1
#
# Write a function electricity(rate_per_unit).
#
# -   The outer function receives the cost per unit.
# -   The inner function receives the number of units consumed.
# -   Print the total electricity bill.
# -   Return the inner function.


def electricity(rate_per_unit):
    def inner(units):
        print(rate_per_unit*units)
    return inner
l=electricity(30)
l(2)


# Question 2
#
# Write a function salary(bonus).
#
# -   The outer function receives the bonus amount.
# -   The inner function receives the employee’s basic salary.
# -   Print the total salary after adding the bonus.
# -   Return the inner function.


def salary(bonus):
    def inner(salary):
        print(salary+bonus)
    return inner
l=salary(200)
l(2000)



# Question 3
#
# Write a function discount(percent).
#
# -   The outer function receives the discount percentage.
# -   The inner function receives the product price.
# -   Print the final price after applying the discount.
# -   Return the inner function.


def discount(percent):
    def price(product_price):
        final_price=product_price-(product_price*percent/100)
        print(final_price)
    return price
l=discount(10)
l(1000)

#
# Question 4
#
# Write a function bank_account(balance).
#
# -   The outer function receives the initial balance.
# -   The inner function receives an amount to withdraw.
# -   Print the remaining balance.
# -   Return the inner function.

def bank_account(balance):
    def withdraw(w_amount):
        print(balance-w_amount)
    return withdraw
l=bank_account(1000)
l(500)


# Question 5
#
# Write a function movie(movie_name).
#
# -   The outer function stores the movie name.
# -   The inner function receives the person’s name.
# -   Print that the person booked a ticket for the movie.
# -   Return the inner function.

def movie(movie_name):
    def person(p_name):
        print(f"{p_name} booked a ticket for the {movie_name}")
    return person
l=movie('sahaa')
l("Akshitha")



# Question 6
#
# Write a function multiplier(number).
#
# -   The outer function receives one number.
# -   The inner function receives another number.
# -   Print their multiplication.
# -   Return the inner function.


def multiplier(number):
    def inner(n):
        print(number*n)
    return inner
l=multiplier(10)
l(2)


# Question 7
#
# Write a function restaurant(food_item).
#
# -   The outer function stores the food item.
# -   The inner function receives the quantity.
# -   Print the order details.
# -   Return the inner function.

def restaurant(food_item):
    def quantity(q):
        print(f"food item:{food_item}")
        print(f"quantity:{q}")
    return quantity
l=restaurant("dosa")
l(3)


# Question 8
#
# Write a function create_password(password).
#
# -   The outer function stores the original password.
# -   The inner function receives another password.
# -   If both passwords are the same, print Access Granted; otherwise
#     print Access Denied.
# -   Return the inner function.

def create_password(password):
    def inner(another_password):
        if password==another_password:
            print("Access Granted")
        else:
            print("access denied")
    return inner
l=create_password("Akshi123")
l("akshi")

#
# Question 9
#
# Write a function shopping_cart(item_name).
#
# -   The outer function receives the item name.pe
# -   The inner function receives:
#     -   quantity
#     -   price per item
# -   Print the item name, quantity, and total price.
# -   Return the inner function.

def shopping_cart(items_name):
    def inner(quantity,price_per_item):
        print(f"item name:{items_name}")
        print(f"quantity:{quantity}")
        print(f"Totalprice:{price_per_item*quantity}")
    return inner
price=shopping_cart("pen")
price(10,5)

# Question 10
#
# Create a function counter().
#
# -   Inside it, initialize a variable count = 0.
# -   Create an inner function that increments count by 1 every time it is
#     called and prints the updated value.
# -   Return the inner function.
# -   Call the returned function five times.

def counter():
    c=0
    def inner():
        nonlocal c
        c+=1
        print(c)
    return inner
ct=counter()
ct()
ct()
ct()
ct()
ct()



# notes codes

def outer(x):
    def inner():
        print(x*200)
    return inner
l=outer(3)
m=outer(2)
l()
m()


def mul(x):
    def inner(y):
        return x*y
    return inner
double=mul(2)
triple=mul(3)
print(double(2))
print(triple(3))


def mul(x):
    def inner(y,a=None):
        if a:
            nonlocal x
            x=a
        return x*y
    return inner
d=mul(2)
t=mul(3)
print(d(2,10))#assign x=a 2=10
print(t(3))


def outer(func):
    def inner(n):
        print("hii")
        func(n)
    return inner
def greet(name):
    print(f"hello {name}")
l=outer(greet)
l("akshi")


