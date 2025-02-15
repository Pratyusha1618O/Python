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

for name, run in sorted_dict.items():
    print(f"{name}: {run} runs")


# (b) Display name of the batsman with maximum runs.
max_run = max(batsman, key=batsman.get)
print(f"\nBatsman with max run: {max_run}: {batsman[max_run]} run")



# (c) Display only the names of batsmen.
print("\nList of all batsmen:")
for name in batsman.keys():
    print(name)



# (d) Add a new batsman.
new_batsman = "Rinku"
new_run = 546
batsman[new_batsman] = new_run
print(f"\nNew Batsman added: {new_batsman}: {batsman[new_batsman]} runs")



# (e) Remove the batsman having lowest runs.
min_batsman = min(batsman, key=batsman.get)
batsman.pop(min_batsman)
print(f"\nRemoved batsman with lowest run: {min_batsman}")


# Final list of batsmen after all changes
print("\nFinal List of Batsman:")
for name, runs in batsman.items():
    print(f"{name}: {runs} runs")

