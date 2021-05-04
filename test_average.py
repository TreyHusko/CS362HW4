import unittest
import average

class testCaseAverage(unittest.TestCase):
    def test_average(self):
        l = [0]
        self.assertRaises(IndexError, average.Avg, l)
    def test_average2(self):
        l = []
        self.assertRaises(IndexError,average.Avg, l)
    def test_average3(self):
        l = [2, 'dog', 4]
        self.assertRaises(TypeError, average.Avg, l)

if __name__ == "__main__":
    unittest.main()