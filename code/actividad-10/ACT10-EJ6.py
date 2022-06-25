alturas = []

def Verificacion():
    mayores = 0
    menores = 0

    for altura in range(5):
        altura_persona = float(input("Altura > "))
        alturas.append(altura_persona)
        promedio = sum(alturas) / len(alturas)
        
        if alturas[altura] > promedio:
            mayores += 1
        else:
            if alturas[altura] < promedio:
                menores += 1

    print(f"""
            {alturas} | P: {promedio} | Personas altas: {mayores} | Personas bajas: {menores}
            """)
    
if __name__ == '__main__':
    Verificacion()
