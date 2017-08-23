import unittest
import arithmetic

class MyAppUnitTestCase(unittest.TestCase):

    def test_adder(self):
        assert arithmetic.adder(2, 3) == 5


if __name__ == "__main__":
    unittest.main()