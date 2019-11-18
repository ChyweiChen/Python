# PROGRAM ExceptionHandling
try:
    InputValue = int(input("Please Input a Value:  "))
except ValueError:
    print("Dude, you didn't type in a number!")
else:
    print("The value input was", InputValue)
# END.
