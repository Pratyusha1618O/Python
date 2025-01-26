# 1. Write a Python function expanding (numlist), that takes as argument a list of integers, numlist[], and
# returns True if the absolute difference between each adjacent pair of elements strictly decreases; and
# False otherwise. Write a driver program to test the function. The function should handle necessary
# validation checks.
# Example : [2, 3, 5, 9, 15, 24] returns False
# [2, 3, 4, 6] returns False
# [2, 10, 16, 20] returns True

def expanding(numlist):
    l = len(numlist)

    #validation check for input list
    if l < 2:
        return False
    
    #list to hold absolute differences
    differences = []

    #Calculate absolute differences between adjacent elements
    for i in range(l-1):
        diff = abs(numlist[i] - numlist[i+1])
        differences.append(diff)

    #Check if the differences are strictly decreasing
    for i in range(1, len(differences)):
        if differences[i] >= differences[i-1]:
            return False
    return True

if __name__ == "__main__":
    test_cases = [
        [2, 3, 5, 9, 15, 24],  # Expected: False
        [2, 3, 4, 6],          # Expected: False
        [2, 10, 16, 20],       # Expected: True
        [5, 3, 1, -1],         # Expected: True
        [4, 2, 4, 1],          # Expected: False
        [10, 8],               # Expected: True
        [1],                   # Expected: False
        []                     # Expected: False
    ]

    
    for case in test_cases:
        result = expanding(case)
        print(f"Expanding({case}) = {result}")


    # User Input

    # test_case = []
    # n = int(input("Enter the no. of elem: "))
    # print("Enter list elem: ")
    # for i in range(n):
    #     elem = int(input())
    #     test_case.append(elem)

    # result = expanding(test_case)
    

