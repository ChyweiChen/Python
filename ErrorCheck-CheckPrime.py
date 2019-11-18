# PROGRAM CheckPrime:

##################
# ERROR CHECKING #
##################
c = str(input("Do you want error checking on? (y/n)"))
if c == 'y':
# THEN
    MyErrorCheck = True
else:
    MyErrorCheck = False
# ENDIF;

##################
# PRIME CHECKING #
##################

a = int(input("Please input value:"))
b = a - 1
IsPrime = True
while b != 1:
# DO
    if a % b == 0:
        # THEN
        IsPrime = False
        if MyErrorCheck == True:
        # THEN
            print("****** Division with no remainder found, with ", b, "*********")
        # ENDIF;
    # ENDIF;
    if MyErrorCheck == True:
    # THEN
        print(">> a is ",a,">> b is ",b, ">> IsPrime is ",IsPrime)
    # ENDIF;
    b = b - 1
# ENDWHILE;
if IsPrime:
# THEN
    print(a, "is a prime number")
else:
    print(a, "is not a prime number")
# ENDIF;
# END.
