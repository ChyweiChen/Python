# PROGRAM String Preprocessing

keep = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        ' ', '-', "'"}

######### MODULE Normalise #########

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


######### Main Program #########

Quote = "A long time ago in a galaxy far, far away ..."
NewQuote = Normalise(Quote)
print(Quote)
print(NewQuote)

################################
