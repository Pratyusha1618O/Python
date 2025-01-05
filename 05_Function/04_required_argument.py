## Required Argument

def func(name):
    msg = "Hi "+ name
    return msg
name = input("Enter name: ")
print(func(name))

##Simple interest // here using required argument 
def simple_interest(p,t,r):   
    return (p*t*r)/100   
p = float(input("Enter the principle amount: "))   
r = float(input("Enter the rate of interest: "))   
t = float(input("Enter the time in years: "))   
print("Simple Interest: ",simple_interest(p,r,t)) 