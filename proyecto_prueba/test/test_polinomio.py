'''
Created on 7/8/2014

@author: Jean Carlos
'''
import unittest

from polinomio import buscar_raices, buscar_coeficientes, \
                      NoEsFuncionCuadratica, \
                      NoExistenRaicesReales


class TestPolinomio(unittest.TestCase):

    def test_buscar_raices(self):
        COEFICIENTES_RAICES = [
            ((1,0,0), (0, 0)),
            ((-1,1,2), (-1, 2)),
            ((-1,0,4), (-2, 2)),
        ]
        for coef, raices_esperadas in COEFICIENTES_RAICES:
            raices = buscar_raices(coef[0], coef[1], coef[2])
            self.assertEquals(raices, raices_esperadas)

    def test_formar_poliniomio(self):
        RAICES_COEFICIENTES = [
            ((1, 1), (1, -2, 1)),
            ((0, 0), (1, 0, 0)),
            ((2, -2), (1, 0, -4)),
            ((-4, 3), (1, 1, -12)),
        ]

        for raices, coeficientes_esperados in RAICES_COEFICIENTES:
            coeficientes = buscar_coeficientes(raices[0], raices[1])
            self.assertEquals(coeficientes, coeficientes_esperados)

    def test_no_pudo_encontrar_raices(self):
        self.assertRaises(NoExistenRaicesReales, buscar_raices, 1, 0, 4)

    def test_no_es_cuadratica(self):
        self.assertRaises(NoEsFuncionCuadratica, buscar_raices, 0, 2, 3)

    def test_integridad(self):
        RAICES = [
            (0, 0),
            (1, 2),
            (2.5, 3.5),
            (100, 1000),
        ]
        for r1, r2 in RAICES:
            a, b, c = buscar_coeficientes(r1, r2)
            raices = buscar_raices(a, b, c)
            self.assertEquals(raices, (r1, r2))

    def test_integridad_falla(self):
        COEFICIENTES = [
            (2, 3, 0),
            (-2, 0, 4),
            (2, 0, -4),
        ]
        for a, b, c in COEFICIENTES:
            raices = buscar_raices(a, b, c)
            coeficientes = buscar_coeficientes(raices[0], raices[1])
            self.assertNotEqual(coeficientes, (a, b, c))


if __name__ == '__main__':
    unittest.main()