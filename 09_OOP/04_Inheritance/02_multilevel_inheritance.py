class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

class BabyDog(Dog):
    def weep(self):
        print("Weeping")
    
b = BabyDog()
b.eat()
b.bark()
b.weep()




