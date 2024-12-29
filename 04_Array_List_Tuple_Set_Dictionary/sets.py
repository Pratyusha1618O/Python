x = {1,4,2,3,6}
print(type(x))
print(x)


s = [10,30,60,20]
a = set(s)
a.add(2)
a.discard(10)
a.remove(20)
# a.pop() #random element delete kore debe
# a.clear()
print(a)

A = {1,2,3,4,5,6}
B = {5,6,7,8,9,10}
print(A|B) # Union
print(A & B) # Intersection
# A.intersection(B)

print(A - B) # A te ache B te nei
print(A ^ B) # Set symmetric #Common gulo asbena
# A.symmetric_difference(B)

F = frozenset(['C','Java','Python'])
print(F)

