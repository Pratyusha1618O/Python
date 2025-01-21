try:   
    a = int(input("Enter a:"))     
    b = int(input("Enter b:"))     
    c = a/b   
    print(c)
except Exception as e:   
    print("Can't divide with zero")
    print(e)
else:
    print("Run this code if no exception occurs") 
finally:
    print("Finally always run regardless of exception occurs or not")   