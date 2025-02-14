# (a) Write a Python program to find the power of a number (i.e. NP) using recursion.
# (b) Write a program to create a function "show employee" using the following condition :
# * It should accept the employee's name and salary and display both.


def power(n, p):
    if(p == 0):
        return 1
    return( n * power(n, p-1))

n = int(input("Enter number: "))
p = int(input("Enter power: "))

print(f"{n} ^ {p} = ",power(n, p))

# (b)
def show_employee(name, salary):
    print("Name: ", name)
    print("Salary: ", salary)

name = input("Enter name: ")
sal = input("Enter salary: ")
show_employee(name, sal)