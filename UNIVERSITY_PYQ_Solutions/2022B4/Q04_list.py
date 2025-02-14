# (a) Write a Python program to count Even and Odd number in a List.
# (b) Write a Python function to find the length of a given string.

# (a)
li =[]
n = int(input("No. of list elem: "))
print("Enter list elements: ")
for i in range(n):
    li.append(int(input()))

even_list = [i for i in li if (i%2 == 0)]
odd_list = [i for i in li if (i%2 != 0)]

print("number of evens: ", len(even_list))
print("number of odds: ", len(odd_list))


# (b)
def len_str(str):
    # return len(str)
    count = 0
    for i in str:
        count += 1
    return count

str = input("Enter string: ")
print("Length: ", len_str(str))
