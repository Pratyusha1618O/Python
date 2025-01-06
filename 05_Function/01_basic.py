def sum(a,b):
    return a+b


a = int(input("a = "))
b = int(input("b = "))

print("Sum = ", sum(a,b))

#__________________________________________


def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact

n = int(input("Enter no. : "))
print("factorial: ", fact(n))

