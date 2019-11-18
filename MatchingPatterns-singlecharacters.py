# PROGRAM MatchingPatterns:

import re

def MatchStrings(pattern, search_string):
    match = re.match(pattern, search_string)

    if match:
        template = "'{}' matches pattern '{}'"
    else:
        template = "'{}' does not match pattern '{}'"
    # ENDIF;

    print(template.format(search_string, pattern))
    
# END MatchStrings

################################################

pattern       = "hello wor.d" 
search_string = "hello world"
MatchStrings(pattern, search_string)

################################################

pattern       = "hello wor.d" 
search_string = "hello worxd"
MatchStrings(pattern, search_string)

################################################

pattern       = "hello wor.d" 
search_string = "hello wor d"
MatchStrings(pattern, search_string)

################################################

pattern       = "hello wor.d" 
search_string = "hello word"
MatchStrings(pattern, search_string)

################################################
print("")
################################################

pattern       = "hello wor[lp]d" 
search_string = "hello world"
MatchStrings(pattern, search_string)

################################################

pattern       = "hello wor[lp]d" 
search_string = "hello worpd"
MatchStrings(pattern, search_string)

################################################

pattern       = "hello wor[lp]d" 
search_string = "hello worxd"
MatchStrings(pattern, search_string)

################################################
print("")
################################################

pattern       = "hello wor[a-z]d" 
search_string = "hello world"
MatchStrings(pattern, search_string)

################################################

pattern       = "hello wor[a-zA-Z]d" 
search_string = "hello worLd"
MatchStrings(pattern, search_string)

################################################

pattern       = "hello wor[a-zA-Z0-9]d" 
search_string = "hello wor5d"
MatchStrings(pattern, search_string)

################################################

pattern       = "hello wor[a-zA-Z0-9]d" 
search_string = "hello wor/d"
MatchStrings(pattern, search_string)

################################################
