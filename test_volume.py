import unittest
import volume

class testCaseCube(unittest.TestCase):
    def test_Cube(self):
        self.assertRaises(TypeError, volume.Cube, 1.5, 3.14, 2)
    def test_Cube2(self):
        self.assertRaises(ValueError,volume.Cube, 1, -1, 2)
    def test_Cube3(self):
        self.assertRaises(TypeError, volume.Cube, 'dog', 3, 2)

if __name__ == "__main__":
    unittest.main()