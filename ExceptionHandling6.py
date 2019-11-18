# PROGRAM ExceptionHandling
for InputValue in (None, "Hi!"):
# DO
    try:
        print(float(InputValue))
    except(TypeError, ValueError) as SysMessage:
        print("Something went wrong!")
        print("System Message:", SysMessage)

# ENDFOR;
# END.



