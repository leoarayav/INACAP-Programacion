lista = []

for x in range(5):
    valor = int(input("Ingrese valor: "))
    lista.append(valor)

for k in range(4):
    for x in range(4 - k):
        if lista[x] > lista[x + 1]:
            aux = lista[x]
            lista[x] = lista[x + 1]
            lista[x + 1] = aux

print(f"Lista ordenada de menor a mayor {lista}")

for k in range(4):
    for x in range(4 - k):
        if lista[x] < lista[x + 1]:
            aux = lista[x]
            lista[x] = lista[x + 1]
            lista[x + 1] = aux

print(f"Lista ordenada de mayor a menor {lista}")
