# PROGRAM RecursiveFibonacci 

def RecursiveFib(n):
    if n==1 or n==2:
    # THEN
        return 1
    else:
        return RecursiveFib(n-1)+ RecursiveFib(n-2)
    # ENDIF;
# END RecursiveFibonacci.


######## MAIN PROGRAM #########

InputVal = int(input("Enter number: "))
print (RecursiveFib(InputVal))

# END RecursiveFibonacci.
