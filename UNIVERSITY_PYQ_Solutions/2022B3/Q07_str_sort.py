# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the
# words in a hyphen-separated sequence after sorting them alphabetically.
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow.


str = input("Enter the string: ")

if '-' not in str or not all(part.isalpha() for part in str.split("-")):
    print("Invalid input!")
    exit()
    
sorted_str = ("-".join(sorted(str.split("-"))))
print("Sorted sequence: ", sorted_str)
