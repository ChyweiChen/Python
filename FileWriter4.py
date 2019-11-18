# PROGRAM FileWriter
Message = ["line 1\n", "line 2\n", "line 3\n"]
file_pointer = open("C:\Python34\MyData2.txt", "a")
print(file_pointer.writelines(Message))
file_pointer.close()

# END.
