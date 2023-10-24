import program
import unittest

class TestSum(unittest.TestCase):
    def testchar(self):
        with self.assertRaises(TypeError):
            program.add("a", "b")

if __name__ == '__main__':
    unittest.main()
