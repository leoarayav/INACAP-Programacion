"""
    Ejercicio 5:
        Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos.

    Author:
        Leo Araya | github.com/le01q
"""

def ObtenerPromedios(i: int, j: int, k: int) -> int:
    suma = i + j + k
    promedio = suma / 3
    return print(f"El promedio de los numeros {i}, {j}, {k} es: {promedio}")

ObtenerPromedios(4, 2, 3)