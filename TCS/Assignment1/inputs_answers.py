import unittest
from FSA import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(input_states(), ["on", "off"])
        self.assertEqual(input_alpha(), ["turn_on", "turn_off"])
        self.assertEqual(input_init(), "off")
        self.assertEqual(input_final(), [""])
        self.assertEqual(input_function(), [["off", "turn_on", "off"], ["on", "turn_off", "on"]])


if __name__ == '__main__':
    unittest.main()
