a = []
n = int(input("Enter the no. of elements: "))
print("Enter elements in sorted order: ")
for i in range (0,n):
    elem = int(input())
    a.append(elem)

val = int(input("Enter the value to find: "))
low = 0
high = n-1
mid = (low + high)//2

while(low<=high):
    if(a[mid] < val): low = mid+1
    elif(a[mid] == val): 
        print(val, "found at index",mid)
        break
    else: high = mid-1

    mid = (low+high)//2

if(low>high):
    print("Not found!!",val,"isn't present in the list.")

