import unittest

class CheckNumbers(unittest.TestCase):

    def test_int_float(self):
        self.assertEqual(1, 1.0)
    # END test_int_float
    
    def test_string_float(self):
        self.assertEqual("1", 1.0)
    # END test_string_float

# END CheckNumbers

if __name__ == "__main__":
    unittest.main()
# ENDIF
