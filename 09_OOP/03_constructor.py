## Parameterized
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("Name: ", self.name)
        print("Roll: ", self.age)
    
s = Student("Pro",21)
s.display()   

##____________________________________________________

## non parameterized
class Person:
    def __init__(self):
        print("Pratyusha this side...")

    def show(self, name):
        print("Hello", name)

p = Person()
p.show("Everyone")