## variable length arguments

def printme(*names):
    print("Type of passed argumnets: ",type(names))
    print("Printing passed arguments: ")
    for name in names:
        print(name)

printme("Tithi","Khusi","Raka","Devi")