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
# Matching Strings
################################################

pattern       = "hello world" 
search_string = "hello world"
MatchStrings(pattern, search_string)

################################################
# Non-matching Strings at the end
################################################

pattern       = "hello worl" 
search_string = "hello world"
MatchStrings(pattern, search_string)

################################################
# Non-matching Strings at the start
################################################

pattern       = "ello world" 
search_string = "hello world"
MatchStrings(pattern, search_string)
