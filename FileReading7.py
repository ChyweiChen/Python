# PROGRAM FileReader

file_pointer = open("C:\Python34\MyData.txt", "r")
for line in file_pointer:
    # DO
    print(line)
# ENDFOR;

file_pointer.close()

# END.
