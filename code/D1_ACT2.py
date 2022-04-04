def SumarNumeros(primerNumero, segundoNumero):
    a = primerNumero
    b = segundoNumero

    return a + b

def Programa():
    num1 = int(input("> Primer numero: "))
    num2 = int(input("> Segundo numero: "))
    resultado = SumarNumeros(num1, num2)
    print(f"La suma entre {num1} y {num2} es igual a: {resultado}")

if __name__ == '__main__':
    Programa()
