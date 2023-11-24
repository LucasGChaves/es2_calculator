import unittest

from calculadora import Calculadora


class CalculadoraTest(unittest.TestCase):

    def setUp(self):
        self.calculadora = Calculadora()

    def test_soma(self):
        resultado = self.calculadora.soma(1, 2)
        self.assertEqual(resultado, 3)

    def test_subtracao(self):
        resultado = self.calculadora.subtracao(1, 2)
        self.assertEqual(resultado, -1)

    def test_multiplicacao(self):
        resultado = self.calculadora.multiplicacao(1, 2)
        self.assertEqual(resultado, 2)

    def test_divisao(self):
        resultado = self.calculadora.divisao(1, 2)
        self.assertEqual(resultado, 0.5)

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            self.calculadora.divisao(1, 0)

if __name__ == "__main__":
    unittest.main()