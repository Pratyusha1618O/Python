# Write a program in Python that checks whether any word in a given string starts and ends with a
# vowel. Return true if a word matches the condition; otherwise, return false.
# Sample Data :
# ("Red Orange White") -> True
# ("Red White Black") -> False
# ("abcd dkise eosksu") -> True



def check(spl):
    vowel = ['a', 'e', 'i', 'o', 'u']
    for elem in spl:
        if([i for i in vowel if (elem[0] == i)] and [i for i in vowel if (elem[-1] == i)]):
            return True
    
    return False

str = input("Enter the string: ")
spl = str.split()
print(f"{str} -> {check(spl)}")
