'''
Created on 7/8/2014

@author: Jean Carlos
'''
import math


class NoEsFuncionCuadratica(Exception):
    pass


class NoExistenRaicesReales(Exception):
    pass


def buscar_raices(a, b, c):
    """ Toman los coefeicientes a, b y c de una funcion cuadratica y busca
    sus raices. La funcion cuadratica es del estilo:
        ax**2 + b x + c = 0

    Va a devolver una tupla con las dos raices donde la primer raiz va a ser
    menor o igual que la segunda raiz.
    """
    if a == 0:
        raise NoEsFuncionCuadratica()

    discriminante = b * b - 4 * a * c
    if discriminante < 0:
        raise NoExistenRaicesReales()

    raiz_discriminante = math.sqrt(discriminante)
    primer_raiz = (-1 * b + raiz_discriminante) / (2 * a)
    segunda_raiz = (-1 * b - raiz_discriminante) / (2 * a)

    # min y max son funciones de python
    chico = min(primer_raiz, segunda_raiz)
    grande = max(primer_raiz, segunda_raiz)
    return (chico, grande)


def buscar_coeficientes(primer_raiz, segunda_raiz):
    """ Dada las raices de una funcion cuadratica, devuelve los coeficientes.
    La funcion cuadratica va a estar dada por:
        (x - r1) * (x - r2) = 0
    """
    # a este resultado se llega haciendo las cuentas de distribucion
    return (1, -1 * (primer_raiz + segunda_raiz), primer_raiz * segunda_raiz)

