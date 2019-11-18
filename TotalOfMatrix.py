# PROGRAM TotalOfMatrix:

Ages = [[2,4,7],[3,6,3]]
print(Ages)
total = 0

for n in range(0,2):
# DO
    for m in range(0,3):
    # DO
        total = total + Ages[n][m]
    # ENDFOR;
# ENDFOR;
print("The total value of the matrix is", total)
# END.
