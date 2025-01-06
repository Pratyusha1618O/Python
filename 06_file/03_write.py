## Writing the file 
# To write some text to a file, we need to open the file using the open method with one of the following access modes. 
# w: It will overwrite the file if any file exists. The file pointer is at the beginning of the file. 
# a: It will append the existing file. The file pointer is at the end of the file. It creates a new file if no file exists. 

# write()
fileptr = open("file2.txt","w")
fileptr.write("Happy New year ")
fileptr.close()

fileptr = open("file2.txt","a")
fileptr.write("2025")
