# MAP

def cube(x):
    return x**3

li = [1,2,3,4]
newl = list(map(cube, li))
print("Cube of each elem: ", newl)