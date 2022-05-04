pares = 0
inpares = 0
x = 1

n = int(input("Cuantos numeros vas a ingresar: "))

while x <= n:
    entero = int(input("Ingrese un numero entero: "))

    if entero %2 == 0:
        pares = pares + 1
    else:
        inpares = inpares + 1

