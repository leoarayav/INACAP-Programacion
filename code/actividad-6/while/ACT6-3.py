cont = 0
cont2 = 0
gastos = 0
x = 1

n = int(input("Cantidad empleados: "))

while x <= n:
    sueldo = float(input("> Ingrese el sueldo empleados: "))

    if sueldo <= 300:
        cont = cont + 1
    else:
        cont2 = cont2 + 1
    
    gastos = gastos + sueldo
    x = x + 1

info = f"""
> Cantidad de empleados con el sueldo menor o igual a 300: {cont}
> Cantidad de empleados con el sueldo mayor a 300: {cont2}
"""

print(info)