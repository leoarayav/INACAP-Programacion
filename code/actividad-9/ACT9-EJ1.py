"""
    Ejercicio 1: 
        Desarrollar un programa con 2 funciones, la primera debe solicitar el ingreso de un numero entero
        y mostrar el el cuadrado de dicho valor y la segunda solicita la carga de 2 valores y muestre el producto de los mismos
        llamar desde el bloque del programa a ambas funciones.
    
    Author:
        Leo Araya | github.com/le01q
"""

def MostrarCuadrado(x: int) -> int:
    return x * x

def Producto(x: int, y: int) -> int:
    return x * y

def Solicitud():
    x = int(input("> "))
    y = int(input("> "))
    z = int(input("> "))
    
    accion = input("Selecciona la opcion: (cuadrado | producto): ")

    if accion == "cuadrado":
        return print(MostrarCuadrado(x))

    elif accion == "producto":
        return print(Producto(y, z))

    else:
        print("Error.")

if __name__ == '__main__':
    Solicitud()