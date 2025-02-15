# Write a program in Python to implement a function that reverse elements of a nested-list recursively.
# As for an example-
# ([[1, 2], [3, [4, 5]], 6]).
# Corresponding output should be - [6, [[5, 4], 3], [2, 1]].

import ast

def reverse_list(l):
    if isinstance(l, list):
        return [reverse_list(item) for item in l[::-1]]
    return l


li = []
n = int(input("No. of list elem: "))
print("Enter list elements: ")
for i in range(n):
    li.append(input())

nested_list = ast.literal_eval(li)
reverse = reverse_list(nested_list)
print("Reversed list: ", reverse)


