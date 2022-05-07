negativos = 0
positivos = 0
multiplos_quince = 0
pares = 0

for i in range(1, 11):
    valor = int(input("Ingrese el valor: "))

    if valor < 0: negativos = negativos + 1

    else:
        if valor > 0: positivos = positivos + 1

    if valor % 15 == 0: multiplos_quince = multiplos_quince + 1

    if valor % 2 == 0: pares = pares + valor

    mostrar = f"Negativos: {negativos} | Positivos: {positivos} | Multiplos de 15: {multiplos_quince} | Pares: {pares}"

    print(mostrar)