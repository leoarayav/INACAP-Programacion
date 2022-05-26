"""
    Ejercicio 7: 
        Confeccionar una función que calcule la superficie de un rectángulo y la
        retorne, la función recibe como parámetros los valores de dos de sus lados:

    Example:
        def retornar_superficie(lado1,lado2):
    
    Author:
        Leo Araya | github.com/le01q
"""

def CalcularSuperficie(primerlado: int, segundolado: int) -> int:
    superficie = primerlado * segundolado
    return superficie

CalcularSuperficie(13, 12)
