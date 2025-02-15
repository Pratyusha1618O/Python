# Write a Python program to take a multi word string from user. Then perform the following operations :
# (a) Count the occurrences of a given word in the given string sentence.
# For example :
# Enter string : orange is orange in colour
# Enter word : orange
# Count of the word is : 2
# (b) Form a string where the first character and the last character have been exchanged.
# For example :
# Enter string : hello world
# Modified string : dello worth


# (a) Count the occurrences of a given word in the given string sentence.
from collections import Counter

def count_occurrence(str):
    words = str.split()
    counts = Counter(words)

    word = input("Enter the word: ")
    for elem, count in counts.items():
        if(elem == word):
            print(f"count of the word {elem}: {count}")

str = input("Enter string: ")
count_occurrence(str)


# (b) Form a string where the first character and the last character have been exchanged.
s = input("Enter 2nd string: ")
# first_char = s[0]
# last_char = s[-1]
# rest = s[1:-1]

new_str = s[-1] + s[1:-1] + s[0]
print(new_str)

