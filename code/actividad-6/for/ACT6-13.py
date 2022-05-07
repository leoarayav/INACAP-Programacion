c1 = 0
c2 = 0
c3 = 0
c4 = 0

n = int(input("Cantidad de puntos: "))

for i in range(n):
    x = int(input("X: "))
    y = int(input("Y: "))

    if x > 0 and y > 0:
        c1 = c1 + 1
    else:
        if x < 0 and y > 0:
            c2 = c2 + 1
        else:
            if x < 0 and y < 0:
                c3 = c3 + 1
            else:
                if x > 0 and y < 0:
                    c4 = c4 + 1

mostrado = f"""
Cantidad puntos ingresados en el primer cuadrante: {c1}
Cantidad puntos ingresados en el segundo cuadrante: {c2}
Cantidad puntos ingresados en el tercer cuadrante: {c3}
Cantidad puntos ingresados en el cuarto cuadrante: {c4}
"""

print(mostrado)