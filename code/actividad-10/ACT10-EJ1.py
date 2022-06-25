lista = [6, 178, 135, 189, 43, 13, 57, 98]

def ObtenerNumeros():
    mayor = 0
    for valor in lista:
        print(f"{valor}", end=" ")
        if valor > 100:
            mayor += 1
    print(f"\nNumeros mayores a 100: {mayor}")
    return mayor

if __name__ == '__main__':
    ObtenerNumeros()
