# PROGRAM RecursiveFactorial 

def RecursiveFact(n):
    if n==0:
    # THEN
        return 1
    else:   
        return n * RecursiveFact(n-1)
    # ENDIF;
# END RecursiveFact.


######## MAIN PROGRAM #########

InputVal = int(input("Enter number: "))
print (RecursiveFact(InputVal))

# END RecursiveFactorial.
