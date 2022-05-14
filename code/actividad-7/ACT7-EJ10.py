numero = int(input("> "))

for numero in range(0, 6):
    if numero < 0:
        sumar = numero + numero
        print(f"La suma de los negativos es igual a: {sumar}")
    elif numero > 0:
        positivos = numero + numero
        promedio = positivos / 6
        print(f"El promedio de los positivos es: {promedio}")
    else:
        print("ERROR")
