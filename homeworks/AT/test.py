import unittest
from main import add, subtract, multiply, divide, mod

class TestMath(unittest.TestCase):
   def test_add(self):
       self.assertEqual(add(2, 5),7)
       self.assertNotEqual(add(3, 7), 9)

   def test_subtract(self):
       self.assertEqual(subtract(7, 4), 3)
       self.assertNotEqual(subtract(4, 2), 1)

   def test_multiply(self):
       self.assertNotEqual(multiply(2, 5), 12)
       self.assertEqual(multiply(3, 6), 18)

class TestDivide(unittest.TestCase):
   def test_divide_success(self):
       self.assertEqual(divide(10, 2), 5)
       self.assertEqual(divide(6, 3), 2)
       self.assertEqual(divide(70, 2), 35)

   def test_divide_by_zero(self):
       self.assertRaises(ValueError, divide, 6, 0)

class TestMde(unittest.TestCase):
   def test_mod_success(self):
       self.assertEqual(mod(10, 3), 1)
       self.assertEqual(mod(6, 3), 0)
       self.assertEqual(mod(70, 20), 10)
       self.assertEqual(mod(-5, 3), 1)
       self.assertEqual(mod(7, -3), -2)

   def test_mod_zero(self):
       self.assertRaises(ValueError, mod, 6, 0)

if __name__ == '__main__':
   unittest.main()

