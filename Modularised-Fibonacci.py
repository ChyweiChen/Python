# PROGRAM FibonacciNumbers:

#########################
# Fibonacci Calc Module #
#########################

def CalcFib():
    a = int(input("Please input value: "))
    FirstNum = 1
    SecondNum = 1
    print("Running total: ", SecondNum, " ( 0 + 1 )")
    while a != 1:
    # DO
        total = SecondNum + FirstNum
        print("Running total: ", total, " (",FirstNum,"+",SecondNum,")")
        FirstNum = SecondNum
        SecondNum = total
        a = a - 1
#   # ENDWHILE;
# END.


################
# Main Program #
################

print("Calculating Fibonacci Numbers...")
CalcFib()
# END.
