# Write a Python program that defines a dictionary to store names of 8 batsmen along with number of runs
# they have scored in international cricket. Then do the following :
# (a) Sort the dictionary in descending order of runs.
# (b) Display name of the batsman with maximum runs.
# (c) Display only the names of batsmen.
# (d) Add a new batsman.
# (e) Remove the batsman having lowest runs.

batsman = {}
print("Enter the names and runs: ")
for i in range(8):
    x = input("Name: ")
    y = int(input("Run: "))
    batsman[x] = y


# (a) Sort the dictionary in descending order of runs.
sorted_dict = dict(sorted(batsman.items(), key=lambda x: x[1], reverse=True))

print(sorted_dict)
