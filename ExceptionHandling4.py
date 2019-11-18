# PROGRAM ExceptionHandling
for InputValue in (None, "Hi!"):
# DO
    try:
        print(float(InputValue))
    except(TypeError, ValueError):
        print("Something went wrong!")

# ENDFOR;
# END.



