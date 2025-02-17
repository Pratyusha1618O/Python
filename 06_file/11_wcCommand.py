fileptr = open("file.txt", 'r')

lines = fileptr.readlines()
print(lines)
no_of_lines = len(lines)
print(no_of_lines)

word = sum([len(line.split()) for line in lines])
print(word)

char = sum([len(line) for line in lines])
print(char)

print(fileptr.tell())

fileptr.close()