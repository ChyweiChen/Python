# PROGRAM ExceptionHandling
for InputValue in (None, "Hi!"):
# DO
    try:
        print(float(InputValue))
    except TypeError:
        print("Type Error: Dude, you typed in a NULL value:", InputValue)
    except ValueError:
        print("Value Error: Dude, you typed in alphabetical characters:", InputValue)
# ENDFOR;
# END.



