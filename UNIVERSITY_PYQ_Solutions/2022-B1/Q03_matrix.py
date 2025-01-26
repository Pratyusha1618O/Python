# Write a Python program to perform matrix addition, matrix subtraction, and matrix multiplication by
# simulating matrix as a list of lists. You may use separate functions for each operation.


## Matrix input..........................
def get_matrix(r, c):
    m = []
    for i in range(r):
        row = []
        for j in range(c):
            elem = int(input(f"m[{i}][{j}] = "))
            row.append(elem)
        m.append(row)
    return m

# Matrix Addition.........................
def addition(a, b):
    r = len(a)
    c = len(a[0])
    result = []
    for i in range(r):
        row = []
        for j in range(c):
            elem = a[i][j] + b[i][j]
            row.append(elem)
        result.append(row)
    return result

# Matrix Subtraction.......................
def subtraction(a, b):
    r = len(a)
    c = len(a[0])
    result = []
    for i in range(r):
        row = []
        for j in range(c):
            elem = a[i][j] - b[i][j]
            row.append(elem)
        result.append(row)
    return result


# Matrix Multiplication.....................
def multiplication(a, b):
    r1 = len(a)
    c1 = len(a[0])
    c2 = len(b[0])

    result = []
    for i in range(r1):
        row = []
        for j in range(c1):
            row.append(0)
        result.append(row)
    
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += a[i][k] * b[k][j]
    return result


def main():
    r1 = int(input("Enter row1: "))
    c1 = int(input("Enter col1: "))
    a = get_matrix(r1, c1)

    r2 = int(input("Enter row2: "))
    c2 = int(input("Enter col2: "))
    b = get_matrix(r2, c2)

    print("Matrix 1: ",a)
    print("Matrix 2: ",b)


    #Addition
    if r1 == r2 and c1 == c2:
        print("\nMatrix Addition: ")
        add = addition(a, b)
        print(add)
    else:
        print("addition not possible.")



    # subtraction
    if r1 == r2 and c1 == c2:
        print("\nMatrix subtraction: ")
        sub = subtraction(a, b)
        print(sub)
    else:
        print("Subtraction not possible.")

    # multiplication
    if r2 != c1:
        print("Multiplication not possible.")
    else:
        print("\nMatrix multiplication: ")
        mult = multiplication(a, b)
        print(mult)

if __name__ == "__main__":
    main()

