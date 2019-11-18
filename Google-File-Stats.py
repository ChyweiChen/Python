# PROGRAM File Statistics

def FileStats(filename):
    script = open(filename,'r').read()
    num_chars = len(script)
    num_lines = script.count("\n")
    num_words = len(script.split())

    print("The file '%s' has:" %filename)
    print("    %s characters" %num_chars)
    print("    %s lines" %num_lines)
    print("    %s words" %num_words)

# END FileStats.

######### Main Program #########

FileStats('StarWarsScript.txt')

################################
