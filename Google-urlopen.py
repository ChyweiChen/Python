# PROGRAM Check URL Type

from urllib.request import urlopen  


#### MODULE URL Opener: ####

def URL_Opener(URL_input):
    
    response = urlopen(URL_input)
    
    if response.getheader('Content-Type')=='text/html':
    #THEN
        print("This is a webpage:", URL_input)
        print("#### HEADER INFORMATION: ####")
        webpage1 = response.info()
        print(webpage1)

    else:
        print("This is NOT a webpage:", URL_input)

    # ENDIF

# END Check URL_Opener.


######## MAIN PROGRAM ########

URL_Opener("http://www.damiantgordon.com/nt.pdf")
print(" ")
URL_Opener("http://www.damiantgordon.com/")
print(" ")
URL_Opener("https://docs.python.org/")

# END.

##############################
