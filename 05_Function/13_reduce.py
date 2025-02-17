from functools import reduce

num = [1,2,3,4,5]

def mysum(x, y):
    return x+y

sum = reduce(mysum, num)
print(sum) #15