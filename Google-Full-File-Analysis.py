# PROGRAM File Analysis

keep = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        ' ', '-', "'"}

##### MODULE Normaise String #####

def Normalise(s):
    result = ''

    for x in s.lower(): 
    # DO

        if x in keep:
        # THEN
            result = result + x # Add the current character to result
        # ELSE
            # Do not add the current character to result
        # ENDIF;

    # ENDFOR;

    return result

# END Normalise.

##### MODULE Frequency Count #####

def FreqDict(s):
    NewString = Normalise(s)
    words = NewString.split()
    Dict = {}
    for wordindex in words:
    # DO
        
        if wordindex in Dict:
        # THEN
            Dict[wordindex] = Dict[wordindex] + 1
        else:
            Dict[wordindex] = 1
        # ENDIF;
        
    # ENDFOR;

    return Dict

# END Frequency Count.

##### MODULE File Analysis #####

def FileAnalysis(filename):
    script = open(filename,'r').read()
    num_chars = len(script)
    num_lines = script.count("\n")
    num_words = len(script.split())

    FullDict = FreqDict(script)

    ##### Create an Array from the Dictionary and Sort
    DictArray = []
    for k in FullDict:
    # DO
        pair = (FullDict[k], k)
        DictArray.append(pair)
    # ENDFOR;
    DictArray.sort()
    DictArray.reverse()
    
    print("The file '%s' has:" %filename)
    print("    %s characters" %num_chars)
    print("    %s lines" %num_lines)
    print("    %s words" %num_words)
    print(" ")
    print("The top 20 most occurring words are:")
    i = 1 # i is the number of the list item
    for count, word in DictArray[:20]:
    # DO
        print('%3s. %5s %s' % (i, count, word))
        i = i + 1
    # ENDFOR;

# END File Analysis.

######### Main Program #########

FileAnalysis('StarWarsScript.txt')

################################
