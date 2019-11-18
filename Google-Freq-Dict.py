# PROGRAM Frequency Dictionary

keep = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        ' ', '-', "'"}

##### MODULE Normalise #####

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

######### Main Program #########

Quote = "A long time ago in a galaxy far, far away ..."
NewDict = FreqDict(Quote)
print("Input String:", Quote)
print("Analysis:", NewDict)
################################
