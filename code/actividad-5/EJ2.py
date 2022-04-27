'''
Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete mostrar un
mensaje "Promocionado".
'''

primera_nota = int(input("> Primera nota: "))
segunda_nota = int(input("> Segunda nota: "))
tercera_nota = int(input("> Tercera nota: "))

suma = primera_nota + segunda_nota + tercera_nota
promedio = suma / 3

if promedio >= 7:
    print(f"Su promedio es: {promedio} [APROBADO!]")
else:
    print(f"Su promedio es: {promedio} [REPROBADO!]")