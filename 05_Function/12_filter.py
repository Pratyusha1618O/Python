# FILTER

def filtered(x):
    return x>4

li = [1,2,3,4,5,6,7,8]
filterd_list = list(filter(filtered, li))

print(filterd_list) #[5, 6, 7, 8]