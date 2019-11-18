class OneOnly:
    
    _singleton = None
    
    def __new__(cls, *args, **kwargs):

        if not cls._singleton:
        # THEN
            cls._singleton = super(OneOnly, cls).__new__(cls, *args, **kwargs)
        # ENDIF;
        
        return cls._singleton

    # END __new__

# END OneOnly.

print("Only one created:")
s1 = OneOnly()
print(id(s1))
s2 = OneOnly()
print(id(s2))



class MoreThanOne:
    None
# END MoreThanOne.

print("More than one created:")
s3 = MoreThanOne()
print(id(s3))
s4 = MoreThanOne()
print(id(s4))

