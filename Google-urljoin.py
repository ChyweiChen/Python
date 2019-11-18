# PROGRAM Create URLs

from urllib import parse

webpages_found = ["ContactUs.html", "MainPage.html",
                  "SignUp.html", "FAQ.html"]

#### MODULE URL Joiner: ####

def URL_Joiner(URL_input):
    for PageIndex in webpages_found:
    # DO
        print(parse.urljoin(URL_input, PageIndex))
    # ENDFOR

# END Check URL_Joiner.

######## MAIN PROGRAM ########

URL_Joiner("http://www.damiantgordon.com/index.html")
print(" ")
URL_Joiner("http://www.damiantgordon.com/")
print(" ")
URL_Joiner("https://docs.python.org/")

# END.

##############################
