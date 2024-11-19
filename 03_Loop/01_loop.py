## For Loop

n = int(input("Enter the term: "))

for i in range(0,n):
    print(i)


# 0+1+2+3+.............+n 

a = int(input("Enter the term: "))
s = 0
for i in range(0,a):
    s=s+i
print("The result is: ", s)

# ____________________________________________

## While Loop

print("While loop check: ")
i = 1
while i<6:
    i+=1
    print(i)
    # if(i==3): break
    i += 1
else: ## we can use else after for loop and while loop
    print("End of while")
