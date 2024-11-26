import math
# n = int(input("Enter the number: "))
# copy = n
# sum = 0
# while n>0:
#     r = n % 10
#     sum = sum + math.factorial(r)
#     n = n // 10

# if(sum == copy):
#     print("Krishnamurthy number")
# else:
#     print("Not")

list = []
krishnamurthy_list = []
n = int(input("Enter the number of elements: "))
print("Enter list elements: ")
for i in range(0,n):
    elem = int(input())
    list.append(elem)

for i in list:
    cpy = i
    sum = 0
    
    while i>0:
        r = i % 10
        sum += math.factorial(r)
        i = i // 10
    
    if sum == cpy:
        krishnamurthy_list.append(cpy)
    
print("List of krishnamurthy numbers: ",krishnamurthy_list)


