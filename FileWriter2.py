# PROGRAM FileWriter

file_pointer = open("C:\Python34\MyData2.txt", "w")
print(file_pointer.write("This is a new message\n"))
print(file_pointer.write("This is a second message\n"))
file_pointer.close()

# END.
