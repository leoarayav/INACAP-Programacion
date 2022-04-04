def DeterminarMayor(primerNumero, segundoNumero):
    a = primerNumero
    b = segundoNumero
    
    if a > b:
        print("El numero {} es mayor al {}".format(a, b))
    else:
        print("El numero {} es mayor al {}".format(b, a))

def Interfaz():
    numeroUno = int(input("Ingresa el primer numero: "))
    numeroDos = int(input("Ingresa el segundo numero: "))
    
    DeterminarMayor(numeroUno, numeroDos)

if __name__ == '__main__':
    Interfaz()