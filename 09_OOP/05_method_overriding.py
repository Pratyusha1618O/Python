class Animal:
    def speak(self):
        print("Speaking")

class Dog(Animal): 
    def speak(self): # overriden method: speak
        print("Barking")

d = Dog()
d.speak() #Barking