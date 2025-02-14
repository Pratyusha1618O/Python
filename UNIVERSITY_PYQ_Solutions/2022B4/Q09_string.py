# (a) Write a Python program to reverse order of the words of a given string Example.
# Input str = "my name is lucky"
# output str = "lucky is name my"
# (b) Write a Python program to get the number of occurrences of a specified element in an array.

from collections import Counter

sentence = input("Enter string: ")
# print(sentence[::-1]) ## string reverse
rev_sentence = ' '.join(sentence.split()[::-1])
print(rev_sentence)

#___________________________________________________________________

def count_occurence(arr):
    counts = Counter(arr)

    val = int(input("Enter the number: "))
    for elem, count in counts.items():
        if(elem == val):
            print(f"{elem}: {count}")

arr = [10,20,10,40,50,40,30,60,30,20]
count_occurence(arr)

