################################################

def MergeSort(Age):
    
    print("Splitting ", Age)

    # Keep splitting the array until the is one element in each sub-array
    if len(Age) > 1:
        
    # THEN
        MidPoint = len(Age)//2
        LeftHalf = Age[:MidPoint]
        RightHalf = Age[MidPoint:]

        MergeSort(LeftHalf)
        MergeSort(RightHalf)

        LeftHalfCounter = 0
        RightHalfCounter = 0
        FinishedArrayCounter = 0

        # While there are elements in both the left and right sub-array
        # Keep doing the merge process
        while LeftHalfCounter < len(LeftHalf) and RightHalfCounter < len(RightHalf):
        # DO

            # Put either the next left element or the next right element in the final array
            if LeftHalf[LeftHalfCounter] < RightHalf[RightHalfCounter]:
            # THEN
                Age[FinishedArrayCounter] = LeftHalf[LeftHalfCounter]
                LeftHalfCounter = LeftHalfCounter + 1
            else:
                Age[FinishedArrayCounter] = RightHalf[RightHalfCounter]
                RightHalfCounter = RightHalfCounter + 1
            # ENDIF;
            
            FinishedArrayCounter = FinishedArrayCounter + 1
            
        # ENDWHILE;

        # The previous loop ends when either the left or right sub-array has been added 
        # to the final array, now add the rest of the other array into the final array
        while LeftHalfCounter < len(LeftHalf):
        # DO
            Age[FinishedArrayCounter] = LeftHalf[LeftHalfCounter]
            LeftHalfCounter = LeftHalfCounter + 1
            FinishedArrayCounter = FinishedArrayCounter + 1
        # ENDWHILE;

        while RightHalfCounter < len(RightHalf):
        # DO
            Age[FinishedArrayCounter] = RightHalf[RightHalfCounter]
            RightHalfCounter = RightHalfCounter + 1
            FinishedArrayCounter = FinishedArrayCounter + 1
        # ENDWHILE;
        
    # ENDIF;
    
    print("Merging ", Age)

######## M A I N   P R O G R A M ############

Age = [44,23,42,33,16,54,34,18]
MergeSort(Age)
print(Age)

# END.
