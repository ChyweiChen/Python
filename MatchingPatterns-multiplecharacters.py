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

pattern       = "hel*o" 
search_string = "hello"
MatchStrings(pattern, search_string)

################################################

pattern       = "hel*o" 
search_string = "heo"
MatchStrings(pattern, search_string)

################################################

pattern       = "hel*o" 
search_string = "helllllo"
MatchStrings(pattern, search_string)

################################################
print("")
################################################

pattern       = "[A-Z][a-z]* [a-z]*\." 
search_string = "A string."
MatchStrings(pattern, search_string)

################################################

pattern       = "[A-Z][a-z]* [a-z]*\." 
search_string = "No ."
MatchStrings(pattern, search_string)

################################################

pattern       = "[a-z]*.*" 
search_string = ""
MatchStrings(pattern, search_string)

################################################
print("")
################################################

pattern       = "\d+\.\d+" 
search_string = "0.4"
MatchStrings(pattern, search_string)

################################################

pattern       = "\d+\.\d+" 
search_string = "1.002"
MatchStrings(pattern, search_string)

################################################

pattern       = "\d+\.\d+" 
search_string = "1."
MatchStrings(pattern, search_string)

################################################

pattern       = "\d?\d%" 
search_string = "1%"
MatchStrings(pattern, search_string)

################################################

pattern       = "\d?\d%" 
search_string = "99%"
MatchStrings(pattern, search_string)

################################################

pattern       = "\d?\d%" 
search_string = "999%"
MatchStrings(pattern, search_string)

################################################
print("")
################################################

pattern       = "abc{3}" 
search_string = "abccc"
MatchStrings(pattern, search_string)

################################################

pattern       = "(abc){3}" 
search_string = "abccc"
MatchStrings(pattern, search_string)

################################################

pattern       = "(abc){3}" 
search_string = "abcabcabc"
MatchStrings(pattern, search_string)

################################################
print("")
################################################

pattern       = "[A-Z][a-z]*( [a-z]+)*\.$" 
search_string = "Eat."
MatchStrings(pattern, search_string)

################################################

pattern       = "[A-Z][a-z]*( [a-z]+)*\.$" 
search_string = "Eat more good food."
MatchStrings(pattern, search_string)

################################################

pattern       = "[A-Z][a-z]*( [a-z]+)*\.$" 
search_string = "A good meal."
MatchStrings(pattern, search_string)

################################################
