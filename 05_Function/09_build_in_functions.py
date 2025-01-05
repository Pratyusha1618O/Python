## abs()

# integer    
integer = -20   
print('Absolute value of -20 is:', abs(integer))  # 20
# float
floating = -20.83   
print('Absolute value of -20.83 is:', abs(floating)) #20.83

#_________________________________________________________________

# bin()
## Binary convertion

x = 10
y = bin(x)
print(y)

#_____________________________________________________________

# bytes()

# The python bytes() in Python is used for returning  a bytes object. 
# It is an immutable version of the bytearray() function. 
# It can create empty bytes object of the specified size.

string = "Hello world"
array = bytes(string, 'utf-8')
print(array)

#___________________________________________________________

# callable()
x = 8
print(callable(x)) #false ## x is not callable

#__________________________________________________________

# compile()
code_str = 'x=5\ny=10\nprint("sum =",x+y)'   
code = compile(code_str, 'sum.py', 'exec')   
print(type(code))   # <class 'code'>
exec(code)   # sum = 15
# exec(x) 

#______________________________________________________

# exec()

x = 8   
exec('print(x==8)')   # true
exec('print(x+4)')  # 12

#_____________________________________________________

# sum()

s = sum([1, 2,4 ])   # 7
print(s)   
s = sum([1, 2, 4], 10)   # 17
print(s)

#___________________________________________________

#any()

# The python any() function returns true if 
# any item in an iterable is true. Otherwise, it 
# returns False.

l = [4, 3, 2, 0]                               
print(any(l))    # true                                
l = [0, False]   
print(any(l))   # false
l = [0, False, 5]   
print(any(l))   # true
l = []   
print(any(l))  # false

#_______________________________________________________

#ascii()

normalText = 'Python is interesting'   
print(ascii(normalText))   
otherText = 'Pythön is interesting'  # ö 🙂  
print(ascii(otherText))   
# print('Pyth\xf6n is interesting')  

#__________________________________________________________

# eval()
x = 8   
print(eval('x + 1')) #9

#______________________________________________________________

# format()

# d, f and b are a type   
# integer   
print(format(123, "d"))   
# float arguments   
print(format(123.4567898, "f"))   
# binary format   
print(format(12, "b")) 

#___________________________________________________________________

# getattr()
class Details:   
    age = 22   
    name = "Hiya"   
details = Details()   
print('The age is:', getattr(details, "age"))   
print('The name is:', details.name)  