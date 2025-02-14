# Write a Python function to check whether a string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog".

import string
print(set(string.ascii_lowercase))

def is_pangram(s):
    alphabet = set(string.ascii_lowercase) # Set of all lowercase letters
    s = s.lower() # Convert input string to lowercase
    s = set(s) # Convert input string into a set of unique characters
    return alphabet.issubset(s) # Check if all letters exist in the input


text = input("Enter the text: ")
if(is_pangram(text)):
    print("The string is pangram.")
else:
    print("not pangram")


