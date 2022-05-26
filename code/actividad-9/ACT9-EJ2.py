"""
    Ejercicio 2:
        Desarrollar un programa que solicite la carga de tres valores y muestre el
        menor. Desde el bloque principal del programa llamar 2 veces a dicha
        función (sin utilizar una estructura repetitiva)
    
    Author:
        Leo Araya | github.com/le01q
"""

def ObtenerMenor():
    numeros = []

    for n in range(3):
        numero = int(input("> Numero: ".format(n + 1)))
        numeros.append(numero)
    
    menor = numeros[0]

    for numero in numeros:
        if numero < menor:
            menor = numero
    
    print(f"El menor es el numero: {menor}")

if __name__ == '__main__':
    ObtenerMenor()