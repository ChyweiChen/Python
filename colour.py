class Colour:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self.name = name
    # END __init__
# END class.

redcolour = Colour("#FF0000", "Red")
print(redcolour.name, "is", redcolour.rgb_value)
