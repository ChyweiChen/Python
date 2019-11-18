#########################
# Prime Checking Module #
#########################

def IsItPrime():
    a = int(input("Please input value: "))
    b = a - 1
    IsPrime = True
    while b != 1:
    # DO
        if a % b == 0:
            # THEN
            IsPrime = False
        # ENDIF;
        b = b - 1
    # ENDWHILE;
    return IsPrime

# END IsItPrime.

################
# Main Program #
################

# PROGRAM CheckPrime:

if IsItPrime() == True:
# THEN
    print("Prime number")
else:
    print("Not a prime number")
# ENDIF;

# END.
