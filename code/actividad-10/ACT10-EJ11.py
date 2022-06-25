paises = []

for i in range(5):
    pais = input("Nombre del pais: ")
    paises.append(pais)

for j in range(4):
    for k in range(4-j):
        if paises[k] > paises[k + 1]:
            aux = paises[k]
            paises[k] = paises[k + 1]
            paises[k + 1] = aux

print(f"Listado de paises ordenado alfebaticamente: {paises}")
