# Write a program in Python to use the file data.txt for solving and displaying outputs the following tasks
# after reading it:
# (a) All words ending with "on"
# (b) All words whose second and third letters are "r" and "e"
# (c) All words with no vowels.
import re

fileptr = open("data.txt", 'r')
content = fileptr.read()
print(content)

# (a) All words ending with "on"
str = str(content)
spl = str.split()
print("\nword ends with 'on': ")
for word in spl:
    if word[-2:] == 'on':
        print(word)
# print(spl)


# (b) All words whose second and third letters are "r" and "e"
print("\nwords whose second and third letters are r and e: ")
for word in spl:
    if word[1] == 'r' and word[2] == 'e':
        print(word)

# (c) All words with no vowels.
print("\nAll words with no vowels: ")
no_vowel = [i for i in spl if not re.search(r'[aeiouAEIOU]', i)]
print(no_vowel)

fileptr.close()


