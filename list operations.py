l=[10,20,50,20]
l.append(100)
l.append(700)
print(l)

l1=[1,2,6,8,3,2]
l1.append(l)
print(l1)
l2=[1,2,3,4]
l2.extend(l)
print(l2)

l2.insert(1,20)
print(l2)
l2.insert(20,30)#out of range but add at last
print(l2)


l3=[1,2,3,4,5,2,3,4]
print(l3)
l3.pop()
print(l3)
l3.pop(0)
print(l3)
print(l3.pop(4))#returns the pop value
print(l3)
# l3.pop(10)
# print(l3) #Error

l3.remove(5)
print(l3)
# l3.remove(100)
# print(l3)#Error


l3.clear()
print(l3)


l4=[1,4,3,6,5,4,8,7]#returns the count
print(l4.count(4))

l4.sort()
print(l4)
l4.sort(reverse=True)
print(l4)

l5=[1,5,6,3,6]
l5.reverse()
print(l5)

print(len(l5))

print(l5.index(5))





