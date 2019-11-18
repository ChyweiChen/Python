# PROGRAM ExceptionHandling

NameOfFile = str(input("What File would you like to read:  "))
PathName = "C:\\Python34\\"
Extension = ".txt"
FullFileName = PathName + NameOfFile + Extension
try:
    file_pointer = open(FullFileName, "r")
    print(file_pointer.read())
    file_pointer.close()
except:
    print("No file of that name found")
# END.
