# Write a Python program to calculate the harmonic sum of n - 1.
# Note: The harmonic sum is the sum of reciprocals of the positive integers.
# Example:
#  1 + 1/2 + 1/3 + 1/4 .......

n = int(input("Enter the term: "))
sum = 0
for i in range(1, n):
    sum = sum + (1/i)

print("Sum: ", sum)