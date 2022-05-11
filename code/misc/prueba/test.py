'''
Algunas pruebas dentro de python, archivo solamente de testeo y demostración.
'''

def MostrarCorrecto(test):
    print(f'{test}\t Estado: 🟢')

def MostrarIncorrecto(test):
    print(f'{test}\t Estado: 🔴')

# Ejercicio 1: Multiplicar 2 numeros sin usar el simbolo de multiplicacion (*)

def T_EjercicioUno(funcion):
    '''
    Este es una funcion de prueba para demostrar nuestras soluciones correctas
    Siempre debiese ser así xD
    '''
    if funcion(5, 6) == 5*6:
        MostrarCorrecto(funcion.__name__)
    else:
        MostrarIncorrecto(funcion.__name__)

def MultiplicacionRecursiva(numeroUno, numeroDos):
    if numeroDos == 1:
        return numeroUno
    else:
        return numeroUno + MultiplicacionRecursiva(numeroUno, numeroDos - 1)
T_EjercicioUno(MultiplicacionRecursiva)

def MultiplicacionLoop(numeroUno, numeroDos):
    sum = 0
    
    for i in range(numeroDos):
        sum += numeroUno
    return sum
T_EjercicioUno(MultiplicacionLoop)

# Ejercicio 2: Encontrar el numero mas largo dentro de una lista.

def T_EjercicioDos(funcion):
    if funcion([8, 10, 15, 6, 2, 234]) == 234:
        MostrarCorrecto(funcion.__name__)
    else:
        MostrarIncorrecto(funcion.__name__)

def EncontrarLargoIteracion(num_lista):
    largo = num_lista[0]

    for num in num_lista:
        if largo < num:
            largo = num
    return largo
T_EjercicioDos(EncontrarLargoIteracion)

def EncontrarLargoSimple(num_lista):
    return max(num_lista)
T_EjercicioDos(EncontrarLargoSimple)

def EncontrarLargoRecursiva(num_lista):
    if len(num_lista) == 2:
        if num_lista[0] < num_lista[1]:
            return num_lista[1]
        else:
            return num_lista[0]

        largo_izquierda = num_lista[0]
        largo_derecha = EncontrarLargoRecursiva(num_lista[1:])

        if largo_derecha > largo_izquierda:
            return largo_derecha
        else:
            return largo_izquierda
T_EjercicioDos(EncontrarLargoRecursiva)

# Ejercicio 3: Determinar si todos los caracteres en un string son unicos.

def T_EjercicioTres(funcion):
    if funcion:
        MostrarCorrecto(funcion.__name__)
    else:
        MostrarIncorrecto(funcion.__name__)

def EsUnico(caracteres):
    return len(caracteres) == len(set(caracteres))
T_EjercicioTres(EsUnico)

def EsUnicoSorteado(caracteres):
    previo = ''
    
    for char in sorted(list[caracteres]):
        if char == previo:
            return False
        previo = char
    return True
T_EjercicioTres(EsUnicoSorteado)

def EsUnicoConteo(caracteres):
    for caracter in caracteres:
        if caracteres.count(caracter) > 1:
            return False
    return True
T_EjercicioTres(EsUnicoConteo)

def EsUnicoAlfabetico(caracteres):
    alfabeto = list(set('elperroyelzorrovandirectohaciaelparque'))
    tam_alfabeto = len(alfabeto)
    alfabeto = [c for c in alfabeto if c not in caracteres]
    resultado = (tam_alfabeto - len(caracteres)) == len(alfabeto)
    return resultado

