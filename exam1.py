def student_into(name,*subjects,**details):
    print(f"Name:{name}")
    print(f"Subject:{subjects}")
    print(f"Details:{details}")
    for i,j in details.items():
        print(f"{i}:{j}")
student_into("Akshitha","maths","telugu","biology",grade="A",school="TSMS",rollno="21")

def calculate_percentage(marks):
    p=marks/30*100
    print(f"percentage is {p:.2f}%")
def calculate_grade(marks):
    if  marks>25:
        print("A")
    elif marks>20:
        print("B")
    elif marks>15:
        print("c")
    elif marks>10:
        print("D")
    else:
        print("upgrade")
def process(result_function,marks):
    return result_function(marks)
process(calculate_percentage,20)
process(calculate_grade,30)


add=lambda x,y:x+y
sub=lambda x,y:x-y
mul=lambda x,y:x*y
calc={"add":add,"sub":sub,"mul":mul}
for i  in calc.keys():
    print(i)
user_choice=input("Enter your choice:")
x=int(input("Enter x:"))
y=int(input("Enter y:"))
if user_choice in calc.keys():
    print()
    print(calc[user_choice](x,y))
else:
    print("Invalid Choice")


