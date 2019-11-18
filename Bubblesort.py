# PROGRAM Bubblesort:

Age = [44, 23, 42, 33, 18, 54, 34, 16]

for outerindex in range(0,len(Age)):
# DO
    for index in range(0,len(Age)-1):
    # DO
        if Age[index+1] < Age[index]:
        # THEN
            TempValue = Age[index+1]
            Age[index+1] = Age[index]
            Age[index] = TempValue
        # ENDIF;
    # ENDFOR;
# ENDFOR;
print(Age)
# END.
