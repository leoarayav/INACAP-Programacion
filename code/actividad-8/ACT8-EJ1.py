"""
    Un cine ofrece diversos tipos de películas, según el siguiente menú:

    >> Estreno ($4.200)
    >> Infantil ($2.500)
    >> 3D ($5.500)
    >> Documentales ($1.800)
    >> Finalizar

    Determinar el monto total obtenido por concepto de venta de entradas. El menú se debe
    repetir hasta que se ingrese la opción de finalizar.
"""

VAL_ESTRENO = 4200
VAL_INFANTIL = 2500
VAL_TRIDIMENCIONAL = 5500
VAL_DOCUMENTALES = 1800

MENU_PRINCIPAL = """
Bienvenido al PyCine, porfavor seleccione una opcion:

1. Estreno (Valor: $4.200)
2. Infantil (Valor: $2.500)
3. 3D ($5.500)
4. Documentales ($1.800)
5. Finalizar
"""

ESTRENO = [('El hombre araña', 'Hora: 18:00 PM', 'Sala A10', 'Tiempo estimado: 1hr:30m')]
INFANTIL = [('Shrek Septimo', 'Hora: 19:00 PM', 'Sala A3', 'Tiempo estimado: 1hr:15m')]
TRIDIMENCIONAL = [('Avatar', 'Hora: 15:30 PM', 'Sala A4', 'Tiempo estimado: 2hr:45m')]
DOCUMENTALES = [('Hackers y pirateria', 'Hora: 13:25 PM', 'Sala A7', 'Tiempo estimado: 2hr:15m')]

print(MENU_PRINCIPAL)
opcion = int(input("> "))

if opcion == 5:
    exit()

entradas = int(input("Ingrese cuantas entradas va a comprar: "))

while opcion != 0:
    if opcion == 1:
        print(f"{ESTRENO}")
        total = entradas * VAL_ESTRENO
        print(f"Usted compro {entradas} entradas: [VALOR TOTAL A PAGAR: ${total}]")
        break
    
    elif opcion == 2:
        print(f"{INFANTIL}")
        total = entradas * VAL_INFANTIL
        print(f"Usted compro {entradas} entradas: [VALOR TOTAL A PAGAR: ${total}]")
        break

    elif opcion == 3:
        print(f"{TRIDIMENCIONAL}")
        total = entradas * VAL_TRIDIMENCIONAL
        print(f"Usted compro {entradas} entradas: [VALOR TOTAL A PAGAR: ${total}]")
        break

    elif opcion == 4:
        print(f"{DOCUMENTALES}")
        total = entradas * VAL_DOCUMENTALES
        print(f"Usted compro {entradas} entradas: [VALOR TOTAL A PAGAR: ${total}]")
        break