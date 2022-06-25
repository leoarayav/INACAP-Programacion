cantidad=int(input("Cuantos empleados tiene la empresa?: "))

sueldos=[]

for x in range(cantidad):
    sueldo = int(input("Ingrese sueldo:"))
    sueldos.append(sueldo)

for k in range(cantidad-1):
    for x in range(cantidad - 1 - k):
        if sueldos[x] > sueldos[x + 1]:
            aux = sueldos[x]
            sueldos[x] = sueldos[x + 1]
            sueldos[x + 1] = aux

print(f"Lista de sueldos ordenados {sueldos}")
