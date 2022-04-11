numeros = []

for n in range(3):
    numero = int(input("Introduce el numero #{}: ".format(n + 1)))
    numeros.append(numero)

mayor = numeros[0]
menor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero
    else:
        menor = numero

print("El mayor es {} y el menor es {}".format(mayor, menor))