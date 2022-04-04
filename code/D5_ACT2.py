import math

def Operatoria(altura, radio):
    h = altura
    r = radio

    volumen = math.pi * r * r * h
    area = 2.0 * math.pi * r * (r + h)

    print("Valor del area: " + repr(area))
    print("Valor del volumen: " + repr(volumen))

def DatosEntregados():
    altura = float(input("Ingresa el altura: "))
    radio = float(input("Ingresa el volumen: "))
    Operatoria(altura, radio)

if __name__ == '__main__':
    DatosEntregados()