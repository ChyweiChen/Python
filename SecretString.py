class SecretString:
    '''A not-at-all secure way to store a secret string.'''

    def __init__(self, plain_string, pass_phrase):
        
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase
        
    # End __init__

    def decrypt(self, pass_phrase):
        '''Only show the string if the pass_phrase is correct.'''
        
        if pass_phrase == self.__pass_phrase:
        # THEN
            return self.__plain_string
        else:
            return ''
        # Endif;
        
    # End decrypt.

# End Class.

#################

# The SecretString contains a hidden phrase (plain string) and a pass phrase
secret_string = SecretString("ACME: Top Secret", "Afghanistan banana stand")

# We are calling the object with a pass phrase
print(secret_string.decrypt("Afghanistan banana stand"))

#################

