# PROGRAM CheckPrime:
a = int(input("Please input value:"))
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
if IsPrime == True:
# THEN
    print(a, "is a prime number")
else:
    print(a, "is not a prime number")
# ENDIF;
# END.
