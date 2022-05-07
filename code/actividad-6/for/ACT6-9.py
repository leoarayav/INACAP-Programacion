suma = 0

for i in range(10):
    valor = int(input("Ingrese un numero: "))
    if i >= 5: 
        suma = suma + valor
print(f"Suma de los 5 ultimos numeros: {suma}")