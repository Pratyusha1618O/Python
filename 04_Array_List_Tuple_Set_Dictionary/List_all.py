# Creating a list
my_list = [10, 20, 30, 40, 50]

# Accessing elements
print("First element:", my_list[0])  # Indexing
print("Last element:", my_list[-1])  # Negative Indexing

# Slicing
print("Sliced List (2nd to 4th):", my_list[1:4])

# Adding elements
my_list.append(60)  # Appends at the end
print("After Append:", my_list)

my_list.insert(2, 25)  # Insert at a specific index
print("After Insert:", my_list)

my_list.extend([70, 80])  # Extend the list with another list
print("After Extend:", my_list)

# Removing elements
my_list.remove(30)  # Removes the first occurrence of 30
print("After Remove:", my_list)

popped_element = my_list.pop()  # Removes and returns the last element
print("Popped Element:", popped_element)
print("After Pop:", my_list)

del my_list[2]  # Deletes the element at index 2
print("After Delete:", my_list)

# Searching
print("Index of 40:", my_list.index(40))  # Find index of an element

# Sorting
my_list.sort()  # Ascending order
print("After Sort:", my_list)

my_list.sort(reverse=True)  # Descending order
print("After Reverse Sort:", my_list)

# Reversing a list
my_list.reverse()
print("After Reverse:", my_list)

# Copying a list
copy_list = my_list.copy()
print("Copied List:", copy_list)

# List Comprehension
squared_list = [x**2 for x in my_list]
print("Squared List:", squared_list)

# Length of list
print("Length of List:", len(my_list))

# Checking if an element exists
print("Is 40 in list?", 40 in my_list)

# Clearing the list
my_list.clear()
print("After Clear:", my_list)
