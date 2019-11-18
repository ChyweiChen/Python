# PROGRAM FileWriter

file_pointer = open("C:\Python34\MyData2.txt", "r+")
Current_file = file_pointer.read()
New_file = "Start of file\n" + Current_file

file_pointer.seek(0) # This resets the pointer to the start of the file

file_pointer.write(New_file)

file_pointer.close()

# END.
