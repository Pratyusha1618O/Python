# Write a program in Python to find a pair of elements (index pair) from a given array numbers whose
# sum equals a given target number. This target value is an user input. Report if a solution is found or not.
# Note that, there can be more than one solutions for a target input, so break out when one of them is
# found.
# Input : numbers = [10, 30, 20, 40, 50, 60, 70], target = 50
# Output :
# 0, 3
# 1, 2

numbers = [10, 30, 20, 40, 50, 60, 70]
print(numbers)
target = int(input("Enter the target number: "))
if target not in numbers:
    print("Number not present in list")
    exit()

l = len(numbers)
for i in range(l):
    for j in range(1, l):
        if(numbers[i] + numbers[j] == target):
            a = i
            b = j
            break


print("Index pair: ", a, b)
    
