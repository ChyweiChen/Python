# PROGRAM FileReader

NameOfFile = str(input("What File would you like to read:  "))

PathName = "C:\\Python34\\"
Extension = ".txt"
FullFileName = PathName + NameOfFile + Extension

NumberOfChars = int(input("How many characters do you want to print out:  "))

file_pointer = open(FullFileName, "r")
print(file_pointer.read(NumberOfChars))

file_pointer.close()

# END.
