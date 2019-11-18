# Program make a simple calculator that can
# add, subtract, multiply and divide using functions

#########################################

# MODULE ADD:
def add(x, y):
   """This function adds two numbers"""
   return x + y
# END ADD.

#########################################

# MODULE SUBTRACT:
def subtract(x, y):
   """This function subtracts two numbers"""
   return x - y
# END SUBTRACT.

#########################################

# MODULE MULTIPLY:
def multiply(x, y):
   """This function multiplies two numbers"""
   return x * y
# END MULTIPLY.

#########################################

# MODULE DIVIDE:
def divide(x, y):
   """This function divides two numbers"""
   return x / y
# END DIVIDE.

#########################################
# MAIN PROGRAM
#########################################

print("Select Operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice:")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")
#ENDIF
#########################################

# END.
