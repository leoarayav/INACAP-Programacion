"""
    Ejercicio 6:
        Elaborar una función que nos retorne el perimetro de un cuadrado
        pasando como parámetros el valor de un lado.
    
    Author:
        Leo Araya | github.com/le01q
"""

def PerimetroLado(lado: int) -> int:
    perimetro = lado * 4
    print(f"El perimetro es {perimetro}")

PerimetroLado(12)