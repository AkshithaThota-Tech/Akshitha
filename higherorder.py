employees=[("Rahul",25000),("Anjali",40000),("Kiran",32000),("Sneha",55000)]
k=list(map(lambda x:(x[0],x[1]*1.10),employees))
print(k)


movies=[("Inception",8.8),("Avatar",7.5),("Intersteller",8.7),("Movies X",5.9),("Movies y",6.4)]
k=list(filter(lambda x:x[1]>7.5,movies))
print(k)


prices=[499,1299,250,799,1599]
def calculate_bill(fr,price):
    from functools import reduce
    bill=reduce(fr,prices)
    if bill>=3000:
        bill*=0.9
        return bill
print(calculate_bill(lambda x,y:x+y,prices))



students=[("Arjun",78),("Priya",95),("Kiran",82),("divya",91)]
res=sorted(students,key=lambda x:x[1],reverse=True)
print(res)



products=[("Laptop",55000,4.5),("Mouse",800,4.2),("Keywors",2500,3.8),("Monitor",15000,4,7),("Headphones",3000,4.0)]
selected_products=list(filter(lambda x:x[2]>=4.0,products))
discount=list(map(lambda x:(x[0],x[1]*0.90,x[2]),selected_products))
sor=sorted(discount,key=lambda x:x[1])
from functools import reduce
total_price=reduce(lambda x,y:x+y[1],discount,0)
print(total_price)


delivery=[("D101",5,120),("D102",12,300),("D103",3,80),("D104",15,450),("D105",8,200)]
delivery=list(filter(lambda x:x[1]>5,delivery))
bonus=list(map(lambda x:(x[0],x[1],x[2]+50),delivery))
charges_order=sorted(bonus,key=lambda x:x[1],reverse=True)
from functools import reduce
total_revenue=reduce(lambda x,y:x+y[2],charges_order,0)
print(total_revenue)

l=[1,2,3,4,5,6,7]
# even=list(filter(lambda x:x%2,l))
multi=list(map(lambda x:x*2,(filter(lambda x:x%2==0,l))))
print(multi)
