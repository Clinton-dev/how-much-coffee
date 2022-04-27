import unittest
from coffee import how_much_coffee

class TestCoffee(unittest.TestCase):

    def test_how_much_coffee(self):
        self.assertEqual(how_much_coffee([]), 0)
        self.assertEqual(how_much_coffee(['cw']), 1)
        self.assertEqual(how_much_coffee(['CW']), 2)
        self.assertEqual(how_much_coffee(['cw','CAT']), 3)
        self.assertEqual(how_much_coffee(['cw','CAT','DOG']), 'You need extra sleep')
        self.assertEqual(how_much_coffee(['cw','CAT', 'cw=others']), 3)


if __name__ == "__main__":
    unittest.main()