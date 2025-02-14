# Given a string write a program in Python to find the occurrences of every character, number, 
# special character, punctuations etc.


from collections import Counter

def count_char(s):
    counts = Counter(s)
    print(counts)

    print("Character occurance: ")
    for char, count in counts.items():
        print(f"{char}: {count}")
    
str = input("Enter the string: ")
count_char(str)