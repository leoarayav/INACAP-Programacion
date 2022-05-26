"""
    Ejercicio 8: 
        En el bloque principal del programa cargar los lados de dos rectángulos y
        luego mostrar cuál de los dos tiene una superficie mayor.
    
    Author:
        Leo Araya | github.com/le01q
"""

def Superficie(ladouno: int, ladodos: int) -> int:
    superficie = ladouno * ladodos
    return superficie

def MenuInicial():
    lado1 = int(input("Ingrese lado menor del rectangulo: "))
    lado2 = int(input("Ingrese lado mayor del rectangulo: "))

    lado3 = int(input("Ingrese lado menor del rectangulo dos: "))
    lado4 = int(input("Ingrese lado mayor del rectangulo dos: "))

    if Superficie(lado1,lado2) == Superficie(lado3, lado4):
        print("> Los dos rectangulos tiene la misma superficie")
    else:
        if Superficie(lado1, lado2) > Superficie(lado3, lado4):
            print("El primer rectangulo tiene una superficie mayor")
        else:
            print("El segundo rectangulo tiene una superficie mayor")