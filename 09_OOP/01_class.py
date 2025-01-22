class sample:
    x = 5
print(sample) #<class '__main__.sample'>

S = sample()
print(S.x) #5

#________________________

class people:   #class
    def __init__(self,person, salary):   
        self.person = person   
        self.salary = salary 
         
    def display(self):   
        print(self.person,self.salary)

p = people("Taan", 20000)   #object
p.display()  # Taan 20000




