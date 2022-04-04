import math

def CalcularCateto(primerCateto, segundoCateto):
    x = primerCateto
    y = segundoCateto
    hipotenusa = math.sqrt(x**2) + (y**2)
    print("La hipotenusa segun los dos catetos entregados es: <{}>".format(hipotenusa))

def Introduccion():
    primerCateto = float(input("Ingresa el primer cateto: "))
    segundoCateto = float(input("Ingresa el segundo cateto: "))
    CalcularCateto(primerCateto, segundoCateto)

if __name__ == '__main__':
    Introduccion()