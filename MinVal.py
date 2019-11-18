# PROGRAM MinVal:
Age = [44, 23, 42, 33, 18, 54, 34, 16]
MinVal = Age[0]
for index in range(0,len(Age)):
    # DO
        if MinVal > Age[index]:
        # THEN
            MinVal = Age[index]
        # ENDIF;
    # ENDFOR;
# ENDFOR;
print(MinVal)
# END.
