# (a) Write a program in Python to find all numbers between 1 and N those are divisible by 7 and end
# in 6. Also display their count.
# For example : if N = 60, list of numbers : [56], count = 1.
# (b) Write a program in Python to input different names in any case. Now convert the upper case letters
# to lower case letters and lower case letters to upper case letters.


# (a)
n = int(input("Enter N: "))
li = []
for i in range(1, n+1):
    if(i % 7 == 0):
        if(str(i)[-1] == '6'):
            li.append(i)

print(li)

count = 0
for i in li:
    count += 1
print("Count = ", count)

# (b)
list_name = []
a = int(input("Enter no of elem: "))
print("Enter list elements: ")
for i in range(a):
    list_name.append(input())

new_list = [i.swapcase() for i in list_name]

print("Converted cases: ",new_list)




