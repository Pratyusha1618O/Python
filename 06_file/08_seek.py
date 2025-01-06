# seek()
fileptr = open("file.txt","r")
print("The file pointer is at byte: ", fileptr.tell()) # 0

#file pointer er location 10 kora holo.    
fileptr.seek(10)
print("Now The file pointer is at byte: ", fileptr.tell()) #10
