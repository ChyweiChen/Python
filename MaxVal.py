# PROGRAM MaxVal:
Age = [44, 23, 42, 33, 18, 54, 34, 16]
MaxVal = Age[0]
for index in range(0,len(Age)):
    # DO
        if MaxVal < Age[index]:
        # THEN
            MaxVal = Age[index]
        # ENDIF;
    # ENDFOR;
# ENDFOR;
print(MaxVal)
# END.
