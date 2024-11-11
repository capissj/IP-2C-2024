import unittest
from guia9 import triangle # Reemplazar por el import correspondiente para testear las funciones deseadas

# La clase puede tener otro nombre pero es necesario mantener el unittest.TestCase
class FuncionesTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(triangle(-20, 12, 4), 4, "primer test con a inválido")

    def test_2(self):
        self.assertEqual(triangle(5, -13, 15), 4, "segundo test con b inválido")

    def test_3(self):
        self.assertEqual(triangle(5, 10, 0), 4, "tercer test con c inválido")
    
    def test_4(self):
        self.assertEqual(triangle(0, -10, 15), 4, "cuarto test con a y b inválidos")

    def test_5(self):
        self.assertEqual(triangle(-10, 10, -15), 4, "quinto test con a y c inválidos")
    
    def test_6(self):
        self.assertEqual(triangle(5, 0, 0), 4, "sexto test con b y c inválidos")

    def test_7(self):
        self.assertEqual(triangle(0, 0, 0), 4, "séptimo test con a, b y c inválidos")

    def test_8(self):
        self.assertEqual(triangle(5, 10, 15), 3, "octavo test triángulo con los tres lados de distinta logitud")

    def test_9(self):
        self.assertEqual(triangle(10, 10, 10), 1, "noveno test triángulo con los tres lados iguales")
    
    def test_10(self):
        self.assertEqual(triangle(10, 10, 15), 2, "décimo test con a y b iguales")
    
    def test_11(self):
        self.assertEqual(triangle(15, 22, 15), 2, "onceavo test con a y c iguales")
    
    def test_12(self):
        self.assertEqual(triangle(5, 15, 15), 2, "doceavo test con b y c iguales")
    
    

if __name__ == '__main__':
    unittest.main(verbosity=2)