## Ask the user for two strings, print a new string where the first string is reversed, and the second string is converted to uppercase. Sample string: "Pets", "party", Output: "steP PARTY". Only use string slicing and + operators.

a = input("Enter first string: ")
b = input("Enter second string: ")

reverse = a[::-1]
upper_case = b.upper()

result = reverse + " " + upper_case
print("Output: ", result)