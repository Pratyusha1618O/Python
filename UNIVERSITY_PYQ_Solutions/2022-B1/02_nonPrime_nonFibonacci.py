# Write a Python program to print all non-prime, non-Fibonacci numbers within range a-b, where
# a and b are accepted as command line arguments.

import math
a = int(input("Enter start range: "))
b = int(input("Enter end range: "))

list1 = []
# non prime
for i in range(a, b+1):
    count = 0
    for j in range(1, i+1):
        if(i % j == 0):
            count += 1
    if(count != 2):
        list1.append(i)

print("Non prime numbers: ", list1)

# non fibonacci
list_fib = [0, 1]
x = 0
y = 1
for i in range(2, b):
    z = x+y
    x = y
    y = z
    list_fib.append(z)

list2 = []
for i in range(a, b+1):
    if(i not in list_fib):
        list2.append(i)

print("Fibonacci: ", list_fib)
print("Non Fibonacci: ", list2)

#Non prime non fibonacci
list3 = []
for i in range(a, b+1):
    if(i in list1 and i in list2):
        list3.append(i)

print("Non Prime, Non fibonacci numbers: ", list3)   