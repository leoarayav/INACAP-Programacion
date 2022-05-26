"""
    Ejercicio 9: 
        Plantear una función que reciba un string en mayúsculas o minúsculas y
        retorne la cantidad de letras 'a' o 'A'.
    
    Author:
        Leo Araya | github.com/le01q
"""

def CantidadVocales(palabra: str) -> str:
    vocales = 0
    for v in range(len(palabra)):
        if palabra[v] == "a" or palabra[v] == "A":
            vocales += 1
    return vocales

palabra = input("Ingrese una palabra: ")
print(f"La palabra {palabra} tiene: {CantidadVocales(palabra)} <a>")