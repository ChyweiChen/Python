# PROGRAM BiggerOfThree:
a = int(input("Please input the first value\n"))
b = int(input("Please second the second value\n"))
c = int(input("Please second the third value\n"))

if a > b:
# THEN
       if a > c:
       # THEN
           print(a, "is bigger than", b, " and ", c)
       else:
           print(c, "is bigger than", a, " and ", b)
       # ENDIF;
else:
       if b > c:
       # THEN
           print(b, "is bigger than", a, " and ", c)
       else:
           print(c, "is bigger than", a, " and ", b)
       # ENDIF;
# ENDIF;
# END.
