# Write a Python program to input two sets, S1 and S2 containing names of cities. Then perform the
# following :
# (a) Find union, intersection and symmetric difference of the two sets.
# (b) Display elements of S1 in upper case and S2 in lower case.


# s1 = set()
# print("Enter cities into set1: ")
# while True:
#     elem = input("Enter city(type 'done' to stop): ")
#     if elem == 'done':
#         break
#     s1.add(elem)
# print("set1: ", s1)


## Set operations...................................
def set_operations(s1, s2):
    #UNION
    union = (s1|s2)
    print("\nUnion: ", union)

    #INTESECTION
    intersect = (s1 & s2)
    print("\nInsersection: ", intersect)

    #SYMETRIC DIFFERENCE
    sd = (s1^s2)
    print("\nSymetric Difference: ", sd)


## display..........................................
def set_display(s1, s2):
    #SET1
    uppercase_set = set()
    for elem in s1:
        uppercase_set.add(elem.upper())
    print("\nSet1 in UPPERCASE: ",uppercase_set)

    #SET2
    lowercase_set = set()
    for elem in s2:
        lowercase_set.add(elem.lower())
    print("\nSet2 in LOWERCASE: ", lowercase_set)


#set 1
s1 = set()
n1 = int(input("Enter no. of elements of set1: "))
print("Enter cities into set1: ")
for i in range(n1):
    s1.add(input())

#set2
s2 = set()
n2 = int(input("Enter no. of elements of set2: "))
print("Enter cities into set2: ")
for i in range(n2):
    s2.add(input())


print("Set1: ", s1)
print("Set2: ", s2)

# set operations
set_operations(s1, s2)

#display
set_display(s1, s2)
