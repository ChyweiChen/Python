# PROGRAM Global and Local Variables

global_var = "This is a global variable"

def MyMethod():
    global_var = "This is a local copy of the global variable"
    print(global_var)
    global global_var
    print(global_var)
# END MyMethod

MyMethod()
print(global_var)

#END.
