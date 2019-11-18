class Colour:
    def __init__(self, rgb_value, name):
        self._rgb_value = rgb_value
        self._name = name
    # END _ _init_ _

    def _set_name(self, name):
        self._name = name
    # END set_name

    def _get_name(self):      
        if self._name == "":
            return "There is a blank value"
        else:
            return self._name
        # ENDIF;
    # END get_name

    name = property(_get_name, _set_name)
# END class.

print ("The name is set to RED")
print ("------------------------")
redcolour = Colour("#FF0000", "Red")
print(redcolour.name)
print(redcolour._get_name())

print ("The name is set to blank")
print ("------------------------")
redcolour.name = ""
print(redcolour.name)
print(redcolour._get_name())
