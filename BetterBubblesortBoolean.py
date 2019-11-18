# PROGRAM BetterBubblesortBoolean:

Age = [44, 23, 42, 33, 18, 54, 34, 16]
reducingindex = len(Age)-1
DidSwap = False
for outerindex in range(0,len(Age)):
# DO
    for index in range(0,reducingindex):
    # DO
        if Age[index+1] < Age[index]:
        # THEN
            TempValue = Age[index+1]
            Age[index+1] = Age[index]
            Age[index] = TempValue
            DidSwap = True
        # ENDIF;
    # ENDFOR;
    reducingindex = reducingindex - 1
    if DidSwap == False:
        break
# ENDFOR;
print(Age)
# END.
