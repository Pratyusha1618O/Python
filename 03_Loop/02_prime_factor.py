n = int(input("Enter the number: "))
if(n<=0): print("Please Enter positive number")
else:
    for i in range(1, n+1):
        if(n%i == 0): #factor
            count = 0
            for j in range(1, i+1): #prime
                if(i%j == 0): count += 1
            if(count == 2): print(i)






