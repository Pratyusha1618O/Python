#odd sum
n = int(input("Enter the term: "))
sum = 0
for i in range(1,n+1):
    sum = sum + 2*i - 1
print(sum)
