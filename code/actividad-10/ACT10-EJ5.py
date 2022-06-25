alturas = []

def Cargar():
    for altura in range(5):
        altura_persona = float(input("Altura > "))
        alturas.append(altura_persona)
    print(alturas)

if __name__ == '__main__':
    Cargar()
