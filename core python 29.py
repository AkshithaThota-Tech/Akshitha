from ast import arg


def register_user(username,role="user",*permissions,**details):
    print("UserName:",username)
    print("Role:",role)
    print("Permissions:")
    for i in permissions:
        print(i)
    print("Details:")
    for i,j in details.items():
        print(f"{i}:{j}")
register_user("Akshitha","admin","read","write",age=22,city="sdpt")


def mystery_box(*arg):
   even=arg[::2]
   odd=arg[1::2]
   return even,odd
print(mystery_box("a","b","c","d","e","f"))


def normal_charge(distance):
    return distance*10
def express_charge(distance):
    return distance*20+50
def night_charge(distance):
    return distance*15+30
def calculate_charge(function,distence):
    return function(distence)
print(calculate_charge(normal_charge,8))
print(calculate_charge(express_charge,8))
print(calculate_charge(night_charge,8))


def my(*args):
    even=args[::2]
    odd=args[1::2]
    return even,odd
print(my("a","s","k","j","h"))


def normal_charge(distance):
    return distance*10
def express_charge(distance):
    return distance*20_50
def night_charge(distance):
    return distance*15+30
def calculate_charge(functions,distance):
    return functions(distance)
print(calculate_charge(normal_charge,8))
print(calculate_charge(express_charge,8))
print(calculate_charge(night_charge,8))
