# Take a list from user. Then enter a value to be searched. If the value id present in list, then remove it. Else append it to the list.


def search(list, val):
    count = 0
    for i in list:
        if(i == val): 
            list.remove(val)
            count += 1
    return count

n = int(input("Enter the no. of elements: "))
list = []
for i in range(0,n):
    list.append(int(input()))

print("Original list: ", list)


val = int(input("Enter the value to be searched: "))
new_list = search(list, val)

if(new_list == 1):
    print("New list: ", list)
else:
    list.append(val)
    print("New list: ", list)

