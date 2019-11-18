# PROGRAM SelectionSort:
Age = [44, 23, 42, 33, 18, 54, 34, 16]
print(Age)
for outerindex in range(0,len(Age)):
# DO
    MinValLocation = outerindex
    for index in range(outerindex,len(Age)):
    # DO
        if Age[index] < Age[MinValLocation]:
        # THEN
            MinValLocation = index
        # ENDIF;
    # ENDFOR;
    if MinValLocation != outerindex:
        Age[outerindex], Age[MinValLocation] = Age[MinValLocation], Age[outerindex]
    print(Age, "Value:",Age[outerindex])
# ENDFOR;
# END.
