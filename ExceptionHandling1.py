# PROGRAM ExceptionHanding

try:
    file_pointer = open("C:\Python34\FakeFile.txt", "r")
    print(file_pointer.read())
    file_pointer.close()
except:
    print("Something went wrong")
    
# END.
