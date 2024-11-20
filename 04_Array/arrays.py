from array import*
a = array('i',[1,2,3,4,5])
print(a.index(3)) # 3 er index position
print(a[3]) 

print("___________")
for x in a:
    print(x)

a.insert(1,20) #array('i', [1, 20, 2, 3, 4, 5])
print(a)

a.remove(4) #array('i', [1, 20, 2, 3, 5])
print(a)


a[2] = 80 # array('i', [1, 20, 80, 3, 5])
print(a)

del a[4] # array('i', [1, 20, 80, 3])
print(a)

print(len(a)) # len(arr_name)

#____________________________________________

course = ["C","C++","Java"]

course.append("Python")
print(course)

course.pop(1)
print(course)
