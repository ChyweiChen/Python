#PROGRAM ArraySlicing

Array = [0, 1, 2, 3, 4, 5, 6, 7]

print("Array is", Array)
print("")
print("Array[:3] is", Array[:3])
print("Array[3:] is", Array[3:])
print("")
print("Array[:-3] is", Array[:-3])
print("Array[-3:] is", Array[-3:])
print("")
print("Array[1:5] is", Array[1:5])
print("Array[1:5:2] is", Array[1:5:2])
print("")
print("*******************************")
print("")
MArray = [[0, 1, 2],
          [3, 4, 5],
          [6, 7, 8]]

print("MArray is", MArray)
print("")
print("MArray[:1] is", MArray[:1])
print("MArray[1:] is", MArray[1:])
print("")
print("MArray[:-1] is", MArray[:-1])
print("MArray[-1:] is", MArray[-1:])
print("")
print("MArray[1:2] is", MArray[1:2])
print("MArray[2:3] is", MArray[2:3])

#END ArraySlicing
