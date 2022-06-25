lista = [6, 8, 9, 2, 7]

def Verificacion():
    print(f"{lista}")
    for valor in lista:
        if valor >= 7:
            print(f"{valor}", end=" ")

if __name__ == '__main__':
    Verificacion()
