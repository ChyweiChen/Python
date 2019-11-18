# PROGRAM Insertion Sort:

##################################

def InsertionSort(Age):

   for Index in range(1,len(Age)):
    # DO
     CurrentValue = Age[Index]
     Position = Index

     while Position > 0 and Age[Position - 1] > CurrentValue:
     # DO
     
         Age[Position] = Age[Position - 1]
         Position = Position - 1
     # ENDWHILE;

     Age[Position]=CurrentValue
     print(Age)

    # ENDFOR;

# END InsertionSort.

########## MAIN PROGRAM ##########

Age = [44, 23, 42, 33, 18, 54, 34, 16]
print(Age)
InsertionSort(Age)
print(Age)

# END.
