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
print(my_tuple[1])  #[8, 4, 6]

#___________________________________________________

my_tuple = 3, 4.6, "dog" 
print(my_tuple) 
# tuple unpacking is also possible 
a, b, c = my_tuple 
print(a)     # 3
print(b)     # 4.6
print(c)     # dog

#_____________________________________________________

my_tuple = ('a','b','c','d','e','f','g','h','i')
# 2nd to 4th element
print(my_tuple[1:4]) # ('b', 'c', 'd')

print(my_tuple[:-7]) # ('a', 'b')

print(my_tuple[7:]) # ('h', 'i')


#______________________________________________________

my_tuple = (4, 2, 3, [6, 5]) 
my_tuple[3][0] = 9    # Output: (4, 2, 3, [9, 5]) 
print(my_tuple) 

#______________________________________________________
print((1, 2, 3) + (4, 5, 6)) 
print(("Repeat",) * 3) 
 
print(any(('','0','')))  # any() funtion