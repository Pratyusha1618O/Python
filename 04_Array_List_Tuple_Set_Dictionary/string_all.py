# Creating a string
my_string = "Hello, World!"

# Accessing characters
print("First character:", my_string[0])  # Indexing
print("Last character:", my_string[-1])  # Negative Indexing

# Slicing
print("Sliced String (1st to 5th):", my_string[0:5])

# String Length
print("Length of String:", len(my_string))

# String Concatenation
new_string = my_string + " Welcome to Python."
print("Concatenated String:", new_string)

# String Repetition
repeated_string = "Hello " * 3
print("Repeated String:", repeated_string)

# Checking Substring
print("Is 'World' in string?", "World" in my_string)
print("Is 'Python' not in string?", "Python" not in my_string)

# Changing Case
print("Uppercase:", my_string.upper())
print("Lowercase:", my_string.lower())
print("Title Case:", my_string.title())
print("Swap Case:", my_string.swapcase())
print("Capitalize First Letter:", my_string.capitalize())

# Removing Whitespace
whitespace_str = "   Hello, World!   "
print("Stripped String:", whitespace_str.strip())  # Removes leading & trailing spaces
print("Left Stripped String:", whitespace_str.lstrip())  # Removes leading spaces
print("Right Stripped String:", whitespace_str.rstrip())  # Removes trailing spaces

# Replacing Substring
print("Replaced String:", my_string.replace("World", "Python"))

# Splitting and Joining
split_str = my_string.split(", ")  # Splitting by comma and space
print("Split String:", split_str)

joined_str = "-".join(split_str)  # Joining with a hyphen
print("Joined String:", joined_str)

# Finding Substring
print("Index of 'World':", my_string.find("World"))  # Returns index or -1 if not found
print("Index of 'Python':", my_string.find("Python"))  # Returns -1 (not found)

# Counting Occurrences
print("Count of 'l':", my_string.count("l"))

# Checking String Start/End
print("Starts with 'Hello'?", my_string.startswith("Hello"))
print("Ends with 'World!'?", my_string.endswith("World!"))

# String Formatting
name = "Pratyusha"
age = 21
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print("Formatted String:", formatted_string)

f_string = f"My name is {name} and I am {age} years old."
print("F-String:", f_string)

# Checking if String is Numeric/Alphabetic/Alphanumeric
print("Is '1234' numeric?", "1234".isdigit())
print("Is 'Hello' alphabetic?", "Hello".isalpha())
print("Is 'Hello123' alphanumeric?", "Hello123".isalnum())

# Reversing a String
reversed_string = my_string[::-1]
print("Reversed String:", reversed_string)
