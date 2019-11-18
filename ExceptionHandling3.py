# PROGRAM ExceptionHandling

try:
    InputValue = int(input("Please Input a Value:  "))
    print("The value input was", InputValue)
except ValueError:
    print("Dude, you didn't type in a number!")

# END.
