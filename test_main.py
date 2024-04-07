import unittest
from main import add_two_numbers

class TestMain(unittest.TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(add_two_numbers(5, 3), 8)
        self.assertEqual(add_two_numbers(-1, 1), 0)
        self.assertEqual(add_two_numbers(100, 200), 300)

if __name__ == "__main__":
    unittest.main()