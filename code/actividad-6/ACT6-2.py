suma = 0
x = 1

n = float(input("Ingrese la cantidad de personas a promediar: "))

while x <= n:
    altura = float(input("Ingrese altura de la persona: "))
    suma = suma + altura
    x = x + 1
promedio = suma / n

informacion = f"Altura promedio de las personas: {promedio}"

print(informacion)