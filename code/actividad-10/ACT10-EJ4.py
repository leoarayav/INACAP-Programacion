sueldos = [5.67, 3.13, 5.67, 7.55, 5.43]

def PromedioSueldos():
    print(sueldos)
    for sueldo in sueldos:
        calculo = sum(sueldos) / len(sueldos)
    print(f"> Promedio de los 5 operarios: {calculo}")

if __name__ == '__main__':
    PromedioSueldos()
