# PROGRAM FileBinReader

file_pointer = open("C:\Python34\Python.gif", "br")

first4 = tuple(file_pointer.read(4))

if first4 == (0x47, 0x49, 0x46, 0x38):
    # THEN
    print("This is a GIF file")
else:
    print("This is not a GIF file")
# ENDIF;

file_pointer.close()

# END.
