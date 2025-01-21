try:
    age = int(input("Enter age above 18: "))
    if(age < 18):
        raise ValueError
    else:
        print("Valid")
except ValueError:
    print("Age not valid")