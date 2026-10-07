def calc(x,y,op):
    def add(x,y):
        return x+y
    def sub(x,y):
        return x-y
    def mul(x,y):
        return x*y
    if op=="+":
       return add(x,y)
    elif op=="-":
        return sub(x,y)
    elif op=="*":
        return mul(x,y)
print(calc(10,20,"+"))
print(calc(10,20,"-"))
print(calc(10,20,"*"))
