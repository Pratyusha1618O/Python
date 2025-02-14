# (a) Write a Python program to calculate GCD and LCM of two numbers.
# (b) Write a Python program to create a lambda function that adds 15 to a given number passed in as
# an argument.

# (a)
def gcd(a, b):
    if(a == 0):
        return b
    if(b == 0):
        return a
    return gcd(b, a%b)

def lcm(a, b):
    lcm = abs(a * b) // gcd(a, b)
    return lcm

a = int(input("enter a: "))
b = int(input("enter b: "))

print("GCD: ", gcd(a,b))
print("LCM: ", lcm(a,b))


# (b)
add = lambda x: x+15
n = int(input("Enter number: "))
print("Result: ", add(n))


