class ALife:
    def __init__(self, alife, value):
        self.alife = alife
        self.value = value
    def _get_alife(self):
        print("You are getting a life")
        return self.alife
    def _set_alife(self, value):
        print("You are getting a life {}".format(value))
        self._alife = value
    def _del_alife(self, value):
        print("You have deleted one life")
        del self._alife
    MyLife = property(_get_alife, _set_alife, _del_alife, "DocStrings: This is a life property")
# END class.


NewLife = ALife("long life", "Damian")
NewLife._get_alife()
help(NewLife)
