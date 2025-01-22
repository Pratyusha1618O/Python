class Animal:
    def eat(self):
        print("Eating")

class Pet:
    def play(self):
        print("Playing")

class Dog(Animal, Pet):
    def bark(self):
        print("Barking")
    
d = Dog()
d.eat()
d.play()
d.bark()




