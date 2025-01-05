## Default argument

def printme(name, age=21):
    print("Name: ",name, "Age: ",age)

printme(name="Raj") # the variable age is 
# not passed into the function however the 
# default value of age is considered in the function

##_______________________________________________________________

def printme(name,age=22):   
        print("Name:",name,"Age:",age)
  
printme(name = "Rimi")   
printme(age = 10,name="Taan") #the value of age 
# is overwritten here, 10 will be printed as age