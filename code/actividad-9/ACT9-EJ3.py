"""
    Ejercicio 3:
        Desarrollar una función que reciba un string como parámetro y nos muestre
        la cantidad de vocales. Llamarla desde el bloque principal del programa 3
        veces con string distintos.
    
    Author:
        Leo Araya | github.com/le01q
"""

PALABRA = "Perro"

def ObtenerVocales(palabra: str) -> int:
    palabras = 0
    for vocal in palabra:
        if vocal in "aeiou":
            palabras += 1
    return palabras

cantidad = ObtenerVocales(PALABRA)
print(f"En las palabras {PALABRA} hay {cantidad} vocales") 