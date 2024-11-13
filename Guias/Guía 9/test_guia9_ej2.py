import unittest
from guia9 import min # Reemplazar por el import correspondiente para testear las funciones deseadas

# La clase puede tener otro nombre pero es necesario mantener el unittest.TestCase
class FuncionesTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(min(0, 1), 0, "primer test con x = 0 , y = 1 (x < y)")

    def test_2(self):
        self.assertEqual(min(1, 1), 1, "segundo test con x = 1 , y = 1 (x == y)")

    def test_3(self):
        self.assertEqual(min(2, (-20)), -20, "tercer test con x = 2 , y = -20 (x > y)")
    
if __name__ == '__main__':
    unittest.main(verbosity=2)