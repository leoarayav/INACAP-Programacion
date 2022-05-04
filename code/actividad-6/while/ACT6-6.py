suma = 0
suma2 = 0
x = 1

while x <= 15:
    valor = int(input("Ingrese el valor de la primera lista: "))
    suma = suma + valor
    x = x + 1

x = 1

while x <= 15:
    valor = int(input("Ingrese el valor de la segunda lista: "))
    suma2 = suma2 + valor
    x = x + 1 

if suma > suma2:
    print("Lista 1 mayor")
else:
    if suma2 > suma:
        print("Lista 2 mayor")
    else:
        print("Son iguales!")