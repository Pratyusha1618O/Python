# (a) Write a Python function to remove all occurrences of a given item from a list.
# (b) Write a Python function that takes two lists and returns 'True' if they have at least one common member.

# (a)
def remove_occurrence(lst, elem):
    return [i for i in lst if i != elem]

list1 =[]
l1 = int(input("No. of list1 elem: "))
print("Enter list elements: ")
for i in range(l1):
    list1.append(input())

remove = input("Enter the elem to be removed: ")
new_list1 = remove_occurrence(list1, remove)
print(new_list1)


# (b)

def common_find(lst1, lst2):
    for i in lst1:
        for j in lst2:
            if(i == j):
                return True

    return False


li1 = []
n1 = int(input("No. of first list elem: "))
print("Enter first list elements: ")
for i in range(n1):
    li1.append(input())

li2 = []
n2 = int(input("No. of 2nd list elem: "))
print("Enter 2nd list elements: ")
for i in range(n2):
    li2.append(input())


result = common_find(li1, li2)
print(result)





