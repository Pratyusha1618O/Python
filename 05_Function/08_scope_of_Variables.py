def calculate(*args):   
    sum=0   
    for arg in args:   
        sum = sum +arg   
    print("The sum is",sum) # 60

sum=0   
calculate(10,20,30)   
print("Value of sum outside the function:",sum) #0 