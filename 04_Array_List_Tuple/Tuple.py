# Different types of tuples 

# Empty tuple 
my_tuple = () 
print(my_tuple) 

# Tuple having integers 
my_tuple = (1, 2, 3) 
print(my_tuple) 

# tuple with mixed datatypes 
my_tuple = (1, "Hello", 3.4) 
print(my_tuple) 

# nested tuple 
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3)) 
print(my_tuple) 

#___________________________________________________

my_tuple = 3, 4.6, "dog" 
print(my_tuple) 
# tuple unpacking is also possible 
a, b, c = my_tuple 
print(a)     # 3
print(b)     # 4.6
print(c)     # dog
