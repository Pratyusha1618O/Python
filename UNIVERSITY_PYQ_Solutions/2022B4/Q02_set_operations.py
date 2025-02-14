# (a) Write a Python program to perform the following operations on a set.
# (i) union operation
# (ii) intersection operation
# (iii) set difference operation
# (b) Write a Python program to find maximum number in a set.


# (a)______________________________________________________
s1 = set()
n1 = int(input("Enter no of elem in set1: "))
print("Set1:")
for i in range(n1):
    s1.add(int(input()))

s2 = set()
n2 = int(input("Enter no of elem in set1: "))
print("Set2:")
for i in range(n2):
    s2.add(int(input()))

union = s1 | s2
intersection = s1 & s2
difference = s1 - s2

print("Union: ", union)
print("Intersection: ", intersection)
print("Difference: ", difference)



# (b)_______________________________________________________
a = set()
n = int(input("Enter no of elem in set: "))
print("Set1:")
for i in range(n):
    a.add(int(input()))

set_to_list = sorted(list(a))
print("Maximum number in the set: ", set_to_list[-1])



