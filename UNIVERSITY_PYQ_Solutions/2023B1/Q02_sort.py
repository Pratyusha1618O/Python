# Write a program in Python that fills an empty list with n integers, where n is also an user input. Then
# find the longest chain of monotonically ascending or descending set of values in the list. Here choice
# of ascending or descending order must be inputted by user. Output "NIL" if no such order found in
# list.
# Say : i/p list [1, 3, 0, 2, 3, 4, 5]
# choice ascending, o/p [0, 2, 3, 4, 5]

li = [1, 3, 0, 2, 3, 4, 5]
# n = int(input("No. of list elem: "))
# print("Enter list elements: ")
# for i in range(n):
#     li.append(int(input()))

li = list(set(li))

while(True):
    print("\n")
    print("1. Ascending")
    print("2. Descending")
    print("3. Exit")
    ch = int(input("Enter your choise: "))

    if(ch == 1):
        li.sort()
        print("Ascending: ", li)
    elif(ch == 2):
        li.sort(reverse = True)
        print("Descending: ", li)
    elif(ch == 3):
        exit()
    else:
        print("Wrong choise!!")