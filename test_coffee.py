import unittest
from coffee import Coffee

class TestCoffee(unittest.TestCase):


    self.assert_equals(how_much_coffee([]), 0)
    test.assert_equals(how_much_coffee(['cw']), 1)
    test.assert_equals(how_much_coffee(['CW']), 2)
    test.assert_equals(how_much_coffee(['cw','CAT']), 3)
    test.assert_equals(how_much_coffee(['cw','CAT','DOG']), 'You need extra sleep')
    test.assert_equals(how_much_coffee(['cw','CAT', 'cw=others']), 3)