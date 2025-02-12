# Write a recursive function that finds the H.C.F. of two numbers passed as arguments. Then write a
# Python program to input a list of integers, intlist[] and find the H.C.F. of the first and the fifth elements.
# The program should handle errors like Name Error, Index Error, Zero Division Error and Value Error.

def hcf(a, b):
    if(a == 0):
        return b
    if(b == 0):
        return a
    return hcf(b, a%b)

def lcm(a, b):
    lcm = abs(a*b) // hcf(a,b)
    return lcm


try:
    li = []
    n = int(input("Enter the no of elements: "))

    if(n < 5):
        raise IndexError("List must contain atleast 5 elements.")
    
    print("Enter list elements: ")
    for i in range(0, n):
        elem = int(input())
        li.append(elem)

    hcf_result = hcf(li[0], li[4])
    lcm_result = lcm(li[0], li[4])

    print("HCF: ", hcf_result)
    print("LCM: ", lcm_result)

except ValueError:
    print("ValueError: All inputs must be integer")
except IndexError as ie:
    print("IndexError: ", ie)
except NameError:
    print("NameError: A variable was used before it was defined")
except ZeroDivisionError:
    print("ZeroDivisionError: Can not compute HCF with zero")
except Exception as e:
    print("Exception handled", e)