personas = ["Leo", "Aron", "Rodrigo", "Arturo", "Natalia"]

def ListarPersonas():
    for nombre in personas:
        print(nombre)
    
def ContarCaracteres():
    mayor = 0
    for caracter in personas:
        if len(caracter) >= 5:
            mayor += 1
    print(mayor)

if __name__ == '__main__':
    ListarPersonas()
    ContarCaracteres()
