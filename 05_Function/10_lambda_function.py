# a is an argument and a+10 is an expression which got evaluated and returned.     
x = lambda a:a+10  
print(x)   #<function <lambda> at 0x0000016DAE098AE0>
print("sum = ",x(20))  # sum =  30


#_____________________________________
# map()

lst = [10,20,30,40,50]
sqr_lst = list(map(lambda x:x**2,lst))
# the tuple contains all the items of the list for which the lambda function evaluates to true     
print(sqr_lst) # [100, 400, 900, 1600, 2500]

#_____________________________________
#filter()

lst = [1,2,3,4,5,6]
odd_list = tuple(filter(lambda x:(x%2 != 0),lst))
print(odd_list) #(1, 3, 5)

#_____________________________________
#

