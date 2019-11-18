################################################

def QuickSort(Age):
   MainQuickSort(Age, 0, len(Age) - 1)
# END QuickSort.

################################################
   
def MainQuickSort(Age, First, Last):

   if First < Last:
   # THEN
       splitpoint = Partition(Age, First, Last)
       
       MainQuickSort(Age, First, splitpoint - 1)
       MainQuickSort(Age, splitpoint + 1, Last)

   # ENDIF;

# END QuickSortHelper.

################################################
   
def Partition(Age, First, Last):
   pivotvalue = Age[First]

   Finished = False
   LeftPointer = First + 1
   RightPointer = Last
   
   while not Finished:
    # DO

       # Keep looping within the partition, starting from the left, and
       # moving to the right until we stop at a value that is larger than
       # the PIVOT value, or until we stop at the correct PIVOT position

       while LeftPointer <= RightPointer and Age[LeftPointer] <= pivotvalue:
        # DO
           LeftPointer = LeftPointer + 1
        # ENDWHILE;

       # Keep looping within the partition, starting from the right, and
       # moving to the left until we stop at a value that is smaller than
       # the PIVOT value, or until we stop at the correct PIVOT position

       while Age[RightPointer] >= pivotvalue and RightPointer >= LeftPointer:
        # DO
           RightPointer = RightPointer - 1
        # ENDWHILE;

       if RightPointer < LeftPointer:
        # THEN
           Finished = True
       else:
           # Swap LeftPointer with RightPointer
           # In other words, swap a value less than PIVOT with one that is greater
           temp = Age[LeftPointer]
           Age[LeftPointer] = Age[RightPointer]
           Age[RightPointer] = temp
        # ENDIF;

   # ENDWHILE;

   # Swap First with RightPointer
   # In other words, put the PIVOT value in its correct place
   temp = Age[First]
   Age[First] = Age[RightPointer]
   Age[RightPointer] = temp

   return RightPointer

# END partition.

######## M A I N   P R O G R A M ############
   
Age = [54,26,93,17,77,31,44,55,20]
print(Age)
QuickSort(Age)
print(Age)

# END.
