import unittest

def MyAverage(seq):
    return sum(seq) / len(seq)
# END average


class TestAverage(unittest.TestCase):

    def test_zero(self):
        self.assertRaises(ZeroDivisionError, MyAverage, [])
    # END test_zero

    def test_with_zero(self):
        with self.assertRaises(ZeroDivisionError):
            MyAverage([])
    # END test_with_zero

# END CLASS TestAverage

if __name__ == "__main__":
    unittest.main()
# ENDIF



