import unittest
from guia9 import max # Reemplazar por el import correspondiente para testear las funciones deseadas

# La clase puede tener otro nombre pero es necesario mantener el unittest.TestCase
class FuncionesTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(max(0, 0), 0, "primer test con x = 0 , y = 0 (x == y)")

    def test_2(self):
        self.assertEqual(max(0, 1), 1, "segundo test con x = 0 , y = 1 (x < y)")

    def test_3(self):
        self.assertEqual(max(2, 0), 2, "tercer test con x = 2 , y = 0 (x > y)")
    
if __name__ == '__main__':
    unittest.main(verbosity=2)