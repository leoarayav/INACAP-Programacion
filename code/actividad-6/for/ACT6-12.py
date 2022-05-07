c1 = 0
c2 = 0
c3 = 0

n = int(input("Ingrese la cantidad de triangulos: "))

for t in range(n):
    lado_uno = int(input("Ingrese el lado 1: "))
    lado_dos = int(input("Ingrese el lado 2: "))
    lado_tres = int(input("Ingrese el lado 3: "))

    if lado_uno == lado_uno or lado_uno == lado_dos or lado_uno == lado_tres:
        print("Triangulo equilatero")
        c1 = c1 + 1

    else:
        if lado_uno == lado_dos or lado_uno == lado_tres or lado_dos == lado_tres:
            print("Triangulo isosceles")
            c2 = c2 + 1
        
        else:
            print("Triangulo escaleno")
            c3 = c3 + c1

mostrar = f"Triangulos equilateros: {c1}\nTriangulo isosceles: {c2}\nTriangulo escalenos: {c3}"

print(mostrar)