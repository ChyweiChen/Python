# PROGRAM Global and Local Variables

global_var = 4

def MyMethod():
    global_var = 8
    print(global_var)
# END MyMethod

MyMethod()
print(global_var)

#END.
