import unittest

class CheckNumbers(unittest.TestCase):
    'Create a subclass of the TestCase class'


    def test_int_float(self):
        'This test checks if the integer and real value 1 are equal.'
        self.assertEqual(1, 1.0)
    # END test_int_float

# END CheckNumbers


# Make sure this is being run as a script
if __name__ == "__main__":
    unittest.main()
# ENDIF
