# PROGRAM BinarySearch:

Age = [16, 18, 23, 31, 33, 34, 46, 54]
SearchVal = int(input("Please input the search value: "))

first = 0
last = len(Age)
IsFound = False

while first <= last and IsFound == False:
# DO
    index = (first + last) // 2
    print("First:", first," Middle:",index," and Last:",last,"  >IsFound is",IsFound) 
    if Age[index] == SearchVal:
    # THEN
        IsFound = True
        print("Value found")
    elif Age[index] > SearchVal:
    # THEN
        last = index - 1
    else:
        first = index + 1
    # ENDIF;
# ENDWHILE;
if IsFound == False:
    # THEN
    print("************************")
    print("Array consists of", Age)
    print(SearchVal, "is not in array")
# ENDIF;
# END.
