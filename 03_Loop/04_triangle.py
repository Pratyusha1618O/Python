# 1
# 12
# 123
# 1234

n = int(input("Enter the term: "))

for i in range(1,n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()

for i in range(n):
    for j in range(n-1-i):
        print(" ", end="")
    for k in range(i+1):
        print("*", end=" ")
    print()