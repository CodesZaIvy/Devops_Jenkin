import unittest
from file import sum
 
class Test(unittest.TestCase):
 
     def test_sum(self):
       self.assertEqual(sum(4, 5), 9)

       self.assertEqual(sum(1, 2), 3)

if __name__ == 'main':
    unittest.main()