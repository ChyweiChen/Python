# PROGRAM DecimalToBinaryConversion:

def DecToBin(n):
    if n < 0:
    # THEN
        return 'Must be a positive integer'
    elif n == 0:
        return '0'
    else:
        return DecToBin(n//2) + str(n%2)
    # ENDIF;
# END DecToBin.


########### MAIN PROGRAM ###########

InputVal = int(input("Enter DECIMAL number: "))
print("The number", InputVal, "is",DecToBin(InputVal), "in BINARY")

# END DecimalToBinaryConversion.
