# Write a Python program to create a list (taking values from the user) and count the occurrence of each
# element and then create a dictionary to show the count of each element.
# For example :
# Input :
# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
# Output :
# {11 : 2, 45 : 3, 8 : 1, 23 : 2, 89 : 1}

from collections import Counter

def count_occurence(lst):
    counts = Counter(lst)

    print("Count occurrence: ")
    for elem, count in counts.items():
        print(f"{elem} : {count}")

    print(dict(counts))

li =[]
n = int(input("No. of list elem: "))
print("Enter list elements: ")
for i in range(n):
    li.append(int(input()))

count_occurence(li)
