# Write a Python program to find all anagrams of a string in a given list of strings using lambda.
# Original list of strings :
# ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
# Anagrams of 'abcd' in the above string:
# ['beda', 'cbda', 'adcb']

words = ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
target = "abcd"

is_anagram = lambda word: sorted(word) == sorted(target)

anagram = list(filter(is_anagram, words))
print("Anagrams of 'abcd' in the given list: ", anagram )
