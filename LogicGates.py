######################################################

# PROGRAM Logic Gates Simulation

######################################################

# AND gate simulation
def AND(a,b):
    if a == True and b == True :
        return True
    else: 
        return False
# END AND.    

######################################################

# NAND gate simulation
def NAND(a,b):
    if a == True and b == True:
        return False
    else:
        return True
# END NAND.

######################################################

# OR gate simulation
def OR(a,b):
    if a == True:
        return True
    elif b == True:
        return True
    else:
        return False
# END OR.

######################################################

# XOR gate simulation

def XOR(a,b) :
    if a != b:
        return True
    else:
        return False
# END XOR.

######################################################

# TAUTology gate simulation
def TAUT(a,b):
    return True
# END TAUT.

######################################################

################
# MAIN PROGRAM #
################

print("+----------------------+-------------------+")
print("| XOR Truth Table      |  Result           |")
print("+----------------------+-------------------+")
print ("| A = False, B = False | A XOR B  = ", XOR(False,False),"|")
print ("| A = False, B = True  | A XOR B  = ", XOR(False,True)," |")
print ("| A = True,  B = False | A XOR B  = ", XOR(True,False)," |")
print ("| A = True,  B = True  | A XOR B  = ", XOR(True,True),"|")
print("+----------------------+-------------------+")
print(" ")
print("+----------------------+--------------------+")
print("| NAND Truth Table     |  Result            |")
print("+----------------------+--------------------+")
print ("| A = False, B = False | A NAND B  = ", NAND(False,False)," |")
print ("| A = False, B = True  | A NAND B  = ", NAND(False,True)," |")
print ("| A = True,  B = False | A NAND B  = ", NAND(True,False)," |")
print ("| A = True,  B = True  | A NAND B  = ", NAND(True,True),"|")
print("+----------------------+--------------------+")
