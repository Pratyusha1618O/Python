## Keyword argument

# function func is called with the name and message 
# as the keyword arguments   
def func(name,message):   
    print("printing the message with",name,"and",message)   

func(name = "Raj", message ="hello") ###

## Simple interest // here using keyword argument
def simple_interest(p,t,r):   
    return (p*t*r)/100   
print("Simple Interest: ",simple_interest(t=10,r=10,p=1900))
