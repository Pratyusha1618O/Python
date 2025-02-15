# Consider string S1 = "I Love ICE CREAM". Write a Python program to get the following output for
# string S1.
# (a) Print all the words having occurrences of 'e'
# (b) Output will be "I love ice cream"
# (c) Reverse the string
# (d) Check if S1 starts with 'I'
# (e) Replace 'ICE CREAM' in S1 with 'HOCKEY'.



# (a) Print all the words having occurrences of 'e'
def occurrence(str):
    spl = str.split()

    print("All words having occurrence of 'e' :")
    for elem in spl:
        for i in range(len(elem)):
            if( elem[i] == 'e' or elem[i] == 'E'):
                print(elem)

s1 = "I Love ICE CREAM"
occurrence(s1)

# (b) Output will be "I love ice cream"
print(s1[0] + s1[1:].lower())


# (c) Reverse the string
rev = s1[::-1]
print("Reverse: ",rev)


# (d) Check if S1 starts with 'I'
for i in range(len(s1)):
    if(s1[0] == 'I'):
        print("S1 starts with I")
        break
    else:
        print("S1 not starts with I")
        break

# (e) Replace 'ICE CREAM' in S1 with 'HOCKEY'.
new_str = s1.replace('ICE CREAM', 'HOCKEY')
print("New String: ", new_str)


