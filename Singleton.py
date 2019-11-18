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
