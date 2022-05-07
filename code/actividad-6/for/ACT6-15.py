turno_dia = 0
turno_tarde = 0
turno_noche = 0

for i in range(5):
    edad = int(input("Ingrese la edad: "))
    turno_dia = turno_dia + edad
promedio_dia = turno_dia / 5

for i in range(6):
    edad = int(input("Ingrese la edad: "))
    turno_tarde = turno_tarde + edad
promedio_tarde = turno_tarde / 6

for i in range(11):
    edad = int(input("Ingrese la edad: "))
    turno_noche = turno_noche + edad
promedio_noche = turno_noche / 11

print(f"{promedio_dia} | {promedio_tarde} | {promedio_noche}")

if promedio_dia < promedio_tarde and promedio_dia < promedio_noche:
    print("El turno de mañana tiene un promedio menor de las edades.")
else:
    if promedio_tarde < promedio_noche:
        print("El turno de tarde tiene un promedio menor de edades.")
    else:
        print("El turno de noche tiene un promedio menor de edades.")