a = []
n = int(input("Enter the no. of elements: "))

for i in range(0,n):
    elem = int(input())
    a.append(elem)

print("Your list is: ")
print(a)

#__________________________________________

list = [4,2,5,7,8,9,3,10]
list.remove(2)
del list[0]
len(list)
max(list)
min(list)

print(list)
