# PROGRAM FibonacciNumbers:
a = int(input("Please input value:"))
FirstNum = 1
SecondNum = 1
while a != 1:
# DO
    total = SecondNum + FirstNum
    FirstNum = SecondNum
    SecondNum = total
    a = a - 1
# ENDWHILE;
print(total)
# END.
