import program
import unittest

class TestSum(unittest.TestCase):
  def test(self):
    self.assertEqual(program.add(1,3), 4)

if __name__ == '__main__':
  unittest.main()
