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

#_________________________________________________________________

# hashattr()
# any()

l = [4, 3, 2, 0]                               
print(any(l))                                    
l = [0, False]   
print(any(l))   
l = [0, False, 5]   
print(any(l))   
l = []   
print(any(l)) 

#_________________________________________________________________

# locals()

def localsAbsent():   
    return locals()   
def localsPresent():   
    present = "abc"   
    return locals()   
print('locals Not Present:', localsAbsent())   #{}
print('locals Present:', localsPresent())  # {'present': 'abc'}

#_________________________________________________________________

# map()
def calculateAddition(n):
    return n+n
numbers = (1,2,3,4)
result = map(calculateAddition, numbers)
print(result) # <map object at 0x00000219FB08B220>

# converting map object to tuple
numAdd = tuple(result)
print(numAdd) # (2, 4, 6, 8)

#_________________________________________________________________

# object()
python = object()   
print(type(python))   #<class 'object'>
print(dir(python)) 
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

#_________________________________________________________________

#open()
# opens python.text file of the current directory   
# f = open("sample.txt")   
# specifying full path   
# f = open("E:Python\sample.txt") 

#_________________________________________________________________

#chr()

char = chr(65) #A
print(char)

#_________________________________________________________________

# complex()  
  
a = complex(1) # (1+0j)   
b = complex(1,2) # (1+2j)   

print(a)   
print(b)  

#_________________________________________________________________

# hex()
# decimal to hex
result = hex(1)     
result2 = hex(200)    
  
print(result)   
print(result2)  

#_________________________________________________________________


# oct()
# octal to hex
val = oct(10)     
print("Octal value of 10:",val)  


#_________________________________________________________________


#ord()

# The python ord() function returns an 
# integer representing Unicode code point 
# for the given Unicode character.

# Code point of an integer   
print(ord('8'))   # 56
# Code point of an alphabet    
print(ord('R'))   # 82
# Code point of a character   
print(ord('&'))   # 38


print()
#_________________________________________________________________


# pow()
# positive x, positive y (x**y)   
print(4 ** 2)
print(pow(4, 2)) 

#_________________________________________________________________


