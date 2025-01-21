try:   
    a = int(input("Enter a:"))     
    b = int(input("Enter b:"))     
    c = a/b   
    print(c)
# except:   
#     print("Can't divide with zero")

# except Exception:
#     print(Exception) #<class 'Exception'>

except Exception as e:   
    print("Can't divide with zero")
    print(e)
else:
    print("Run this code if no exception occurs")    