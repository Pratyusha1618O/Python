# Write a Python program to implement binary search.

a = []
n = int(input("No. of list elem: "))
print("Enter list elements: ")
for i in range(n):
    a.append(int(input()))

a = sorted(a)

low = 0
high = n-1
mid = (low + high) // 2
elem = int(input("Enter the elem to be searched: "))

while(low <= high):
    if(a[mid] < elem):
        low = mid+1
    elif(a[mid] == elem):
        print(f"{elem} found at index {mid}")
        break
    else:
        high = mid-1

    mid = (low+high) // 2

if(low > high):
    print("Element not present")

