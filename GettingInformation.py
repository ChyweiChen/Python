# PROGRAM DomainDetection:

import re

def DetectDomain(searchstring):

    pattern = "^[a-zA-Z.]+@([a-z.]*\.[a-z]+)$"

    match = re.match(pattern, searchstring)

    if match != None:
    # THEN
        domain = match.groups()[0]
        print("<<", domain, ">>", "is a legimate domain")
    else:
        print("<<", search_string, ">>", "is not an e-mail address")
    # ENDIF;

# END DetectDomain


search_string = "Damian.Gordon@dit.ie"
print("Checking",search_string,":")
DetectDomain(search_string)
print("")

search_string = "Damian.Gordon@ditie"
print("Checking",search_string,":")
DetectDomain(search_string)
print("")

search_string = "DamianGordon@dit.ie"
print("Checking",search_string,":")
DetectDomain(search_string)
print("")

search_string = "Damian.Gordondit.ie"
print("Checking",search_string,":")
DetectDomain(search_string)
