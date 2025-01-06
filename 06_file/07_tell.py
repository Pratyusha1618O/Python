## File Pointer positions 
# Python provides the tell() method which is used to print the byte number at which the file pointer currently exists.

fileptr = open("file.txt","r")
print("The file pointer is at byte: ", fileptr.tell())

content = fileptr.read()
#after the read operation file pointer modifies. tell() returns the location of the fileptr.      
print("After reading, the filepointer is at:",fileptr.tell()) 
fileptr.close()

# OUTPUT:
# The file pointer is at byte:  0
# After reading, the filepointer is at: 29