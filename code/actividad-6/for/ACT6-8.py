n = int(input("Cuantos triangulos procesara?: "))

cantidad_triangulos = 0

for f in range(n):
    base = int(input("Ingresa el valor de la base: "))
    altura = int(input("Ingrese el valor de la altura: "))
    superficie = base * altura / 2
    print(f"SUPERFICIE: {superficie}")

    if superficie > 12: cantidad_triangulos = cantidad_triangulos + 1

    print(f"Cantidad de triangulos con superficie mayor a 12: {cantidad_triangulos}")