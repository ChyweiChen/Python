# PROGRAM ShellSort:

##################################

def ShellSort(Age):
    
    SubListCount = len(Age)//2
    
    while SubListCount > 0:
    # DO
      for StartPosition in range(SubListCount):          
      # DO
        GapInsertionSort(Age,StartPosition,SubListCount)        
      # ENDFOR;
      
      print("After increments of size", SubListCount, "The list is", Age)
      SubListCount = SubListCount // 2
    # ENDWHILE

# END ShellSort.

##################################

def GapInsertionSort(Age, Start, Gap):
    
    for i in range(Start + Gap, len(Age), Gap):
    # DO
        CurrentValue = Age[i]
        Position = i

        while Position >= Gap and Age[Position - Gap] > CurrentValue:
        #DO
            
            Age[Position] = Age[Position - Gap]
            Position = Position - Gap
        # ENDWHILE;

        Age[Position] = CurrentValue
        print(Age)
        
    # ENDFOR;

# END GapInsertionSort.

########## MAIN PROGRAM ##########

Age = [44,23,42,33,16,54,34,18]
print(Age)
ShellSort(Age)
print(Age)

# END.
