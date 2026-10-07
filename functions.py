def multi(*a):
    m = 1
    for i in a:
        m *= i
    return m

def avg(*a):
    s = 0
    c = 0
    for i in a:
        c +=1
        s += i
    print(f"Avg : {s/c}")

def display(**kwargs):
    for i,j in kwargs.items():
        print(f"{i}: {j}")

# display(name="Vamsi",age=21,gender="male",Course="CSE")
def delivery(price,quantity):
    total = price * quantity
    if total < 200:
        total +=40
    print(f"Total Bill : {total}")

def main(l):
    for i,j in enumerate(l):
        print(f"{i}: {j.__name__}")

l = [multi, avg, display, delivery]
main(l)