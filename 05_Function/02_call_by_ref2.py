## Passing mutable object

#defining function
def change_string(str):
    str = str + "Whats going on"
    print("Printing the string inside function: ", str)

str1 = "Hi there... "
change_string(str1)

print("Printing string outside function: ", str1)