"""
    Ejercicio 3:
        Confeccionar una función que reciba tres enteros y los muestre ordenados
        de menor a mayor. En otra función solicitar la carga de 3 enteros por teclado
        y proceder a llamar a la primer función definida.
    
    Author:
        Leo Araya | github.com/le01q
"""

def OrdenarNumeros(x: int, y: int, z: int) -> int:
    if x < y and x < z:
        if y < z:
            print(x, y, z)
        else:
            print(x, z, y)

    else:
        if y < z:
            if x < z:
                print(y, x, z)
            else:
                print(y, z, x)
        else:
            if x < y:
                print(z, x, y)
            else:
                print(z, y, x)

        
def Interfaz():
    a = int(input("> "))
    b = int(input("> "))
    c = int(input("> "))

    OrdenarNumeros(a, b, c)

Interfaz()