import unittest
import fullName

class testCaseFull(unittest.TestCase):
    def test_full(self):
        self.assertRaises(TypeError, fullName.full, 'CR', 7)
    def test_full2(self):
        self.assertRaises(ValueError, fullName.full, 'CR7', '')
    def test_full3(self):
        self.assertRaises(TypeError, fullName.full, 'Billy Bob', 'Junior')

if __name__ == "__main__":
    unittest.main()