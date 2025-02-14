# Given a string S of lower case characters. The task is to check whether the given string is Heterogram
# or not. A heterogram is a word, phrase, or sentence in which no letter of the alphabet occurs more thanonce. 
# Examples :
# Input : S = "the big dwarf only jumps"
# Output : Yes
# Each letter in the string S has occurred only once. Write a program in Python to perform the said task.



def heterogram(s):
    s = s.replace(" ", "") # remove spaces
    s = s.lower() # Convert to lowercase to handle case insensitivity
    
    if(len(set(s)) == len(s)):
        return "Yes"
    else:
        return "No"

str = input("Enter string: ")
print(heterogram(str))