# Write functions in Python called number_of_factors( ) and list_of_factors( ) that take a positive integer
# and do the following :
# (a) number_of_factors(val) : returns a list of its factors
# (b) list_of_factors(val):returns how many factors the number has.
# Check if input is positive and report if not.


def number_of_factors(n):
    li = []
    for i in range(1,n):
        if(n % i == 0):
            li.append(i)
    
    return li

def list_of_factors(n):
    li = number_of_factors(n)
    count = 0
    for i in li:
        count += 1
    
    return count

n = int(input("Enter the number: "))
li = number_of_factors(n)
print("List of factors: ", li)

num_fact = list_of_factors(n)
print("Number of factors: ",num_fact)

