sueldos_dia = []
sueldos_tarde = []

def Calcular():
    for _ in range(4):
        valor_dia = float(input("[TURNO DIA] Ingresa el sueldo > "))
        valor_tarde = float(input("[TURNO TARDE] Ingresa el sueldo > "))
        sueldos_dia.append(valor_dia) 
        sueldos_tarde.append(valor_tarde)
    
    print(f"Turno mañana: {sueldos_dia} | Turno tarde: {sueldos_tarde}")

if __name__ == '__main__':
    Calcular()
