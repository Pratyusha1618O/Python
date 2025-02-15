# (b) Write a Python program to calculate the cosine series :

# cos x = 1 - (x^2/2!) + (x^4 / 4!) - (x^6/6!)+.........

# For example :
# Enter the value of x in degrees : 0
# Enter the number of terms : 10
# 1.0

import math
x = int(input("Enter the value of x in degrees: "))
n = int(input("Enter the no of terms: "))

x = math.radians(x)

cos_x = 0

for i in range(n):
    term = ((-1)**i) * (x**(2*i)) / math.factorial(2*i)
    cos_x += term

print(cos_x)

