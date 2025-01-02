a = {1:'Yuji', 2:'Nobara', 3:'Megumi'}

print(type(a))
print(a)

print(a[1])
print(a.get(2))

#___________________________________________________________________
## Get function ##

person = {'name':"Phill", 'age':22}
print('name: ', person.get('name'))
print("age: ", person.get('age'))
#value is not provided
print('salary: ', person.get('salary')) # none
#value is provided
print("salary: ", person.get('salary',20000)) # salary:  20000

#____________________________________________________________________

# items()
print(person.items())

#___________________________________________________________________

# pop()
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
elem = sales.pop('apple')
print(sales)

#____________________________________________________________________

# popitem()
student = {1:'Raj', 2:"Sumi", 3:"Arpan"}
student.popitem() # (3, 'Arpan')
print(student)

#____________________________________________________________________

# setdefault()
person = {'name': 'Raka', 'age': 22}
age = person.setdefault('age')
print(age)

#_______________________________________________________________

# update()
d = {1:'Prateek', 2:"Khusi", 3:"Devi"}
d1 = {3: "Raka"}
#updates the value of key 3
d.update(d1)
print(d)

d1 = {4: 'Keya'}
d.update(d1)
print(d)

#__________________________________________________________________

# values()
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
print(sales.values())

#__________________________________________________________________

# all()

# all values true 
l = [1, 3, 4, 5] 
print(all(l))  # True

# all values false 
l = [0, False] 
print(all(l)) # false

# one false value 
l = [1, 3, 4, 0] 
print(all(l)) # false

# one true value 
l = [0, False, 5] 
print(all(l)) #false

# empty iterable 
l = [] 
print(all(l)) #true

print()

#_________________________________________________________________

# Membership Test for Dictionary Keys 
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81} 

print(1 in squares) # true

print(2 not in squares) # true

# membership tests for key only not value  
print(49 in squares) # false

#________________________________________________________

squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81} 
for i in squares:
    print(i) # keys
    print(squares[i]) # values

#________________________________________________________

# Dictionary Comprehension

squares = {x: x*x for x in range(6)}
print(squares)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#..................................
# Even numbers from 1 to 50
dict = {i for i in range(1,51) if (i%2 == 0)}
print(dict)