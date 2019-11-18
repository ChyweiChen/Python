# PROGRAM FibonacciNumbers:

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

a = int(input("Please input value:"))
FirstNum = 1
SecondNum = 1
while a != 1:
# DO
    total = SecondNum + FirstNum
    if MyErrorCheck == True:
    # THEN
        print(">> Countdown is ",a)
        print(">> First Number is ",FirstNum,">> Second Number is ",SecondNum,">> Total is ",total)
    # ENDIF;
    FirstNum = SecondNum
    SecondNum = total
    a = a - 1
# ENDWHILE;
print(total)
# END.
