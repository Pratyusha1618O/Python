# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

# Adding elements
my_set.add(6)  # Adds a single element
print("After Add:", my_set)

# Adding multiple elements
my_set.update([7, 8, 9])
print("After Update:", my_set)

# Removing elements
my_set.remove(3)  # Removes element; raises error if not found
print("After Remove:", my_set)

my_set.discard(4)  # Removes element; does not raise error if not found
print("After Discard:", my_set)

popped_element = my_set.pop()  # Removes and returns an arbitrary element
print("Popped Element:", popped_element)
print("After Pop:", my_set)

# Set Operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1 | set2)  # Union (all elements)
print("Intersection:", set1 & set2)  # Intersection (common elements)
print("Difference (set1 - set2):", set1 - set2)  # Difference (elements in set1 not in set2)
print("Symmetric Difference:", set1 ^ set2)  # Elements in either set but not both

# Checking Membership
print("Is 2 in set1?", 2 in set1)
print("Is 10 in set1?", 10 in set1)

# Checking Subset/Superset
print("Is set1 a subset of set2?", set1.issubset(set2))
print("Is set1 a superset of set2?", set1.issuperset(set2))

# Copying a set
copy_set = set1.copy()
print("Copied Set:", copy_set)

# Clearing a set
my_set.clear()
print("After Clear:", my_set)

# Creating a set from a list (removes duplicates)
list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(list_with_duplicates)
print("Set from List (Unique Elements):", unique_set)
