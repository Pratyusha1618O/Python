# readlines()
fileptr = open("file.txt","r")
lines = fileptr.readlines()
print(lines)

print(len(lines)) # no of lines


fileptr.close()

# ['Hello\n', 'Pratyusha this side...']