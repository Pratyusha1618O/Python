# (a) Write a Python program to print the following pattern. In the following output (n = 3)
#         *
#     *       *
# *               *
#     *       *
#         *
# (b) Write a Python program to check whether a given number is Armstrong.

n = int(input("Enter the term: "))
nsp = n-1 #no of spaces
nst = 1 # no of star
ml = n

for i in range(1, n*2):
    for j in range(nsp):
        print(" ", end="")
    for k in range(nst):
        if(k == 0 or k == nst-1):
            print("*", end="")
        else:
            print(" ", end="")

    if(i < ml):
        nsp -= 1
        nst += 2
    else:
        nsp += 1
        nst -= 2
    
    print()
    