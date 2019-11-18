class Colour:
    def __init__(self, rgb_value, name):
        self._rgb_value = rgb_value
        self._name = name
    # END _ _init_ _

    def set_name(self, name):
        self._name = name
    # END set_name

    def get_name(self):      
        if self._name == "":
            return "There is a blank value"
        else:
            return self._name
        # ENDIF;
    # END get_name
# END class.

print ("The name is set to RED")
print ("------------------------")
redcolour = Colour("#FF0000", "Red")
print(redcolour._name)
print(redcolour.get_name())

print ("The name is set to blank")
print ("------------------------")
redcolour._name = ""
print(redcolour._name)
print(redcolour.get_name())
