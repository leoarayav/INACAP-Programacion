personas = []

for _ in range(5):
    nombre = input("Nombre: ")
    personas.append(nombre)
    menor = personas[0]
    if personas[_] < menor:
        menor = personas[_]

print(f"{personas} | Menor orden alfabetico: {menor}")
