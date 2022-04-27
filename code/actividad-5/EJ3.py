'''
Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar un mensaje
indicando si el número tiene uno o dos dígitos.
(Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)
'''

numero = int(input("Ingrese un valor entre 1 y 99: "))

if numero < 10:
    print(f"{numero} tiene menos de dos digitos")
else:
    print(f"{numero} tiene dos digitos")