n = int(input("Enter the number: "))
copy = n
count = 0
sum = 0

while n>0:
    n = n // 10
    count += 1

n = copy

while n>0:
    r = n % 10
    sum = sum + (r**count)
    n = n // 10

if(sum == copy):
    print("Armstrong number.")
else:
    print("Not an armstrong number.")
