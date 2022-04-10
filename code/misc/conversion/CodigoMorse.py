from Equivalencias import EQUIVALENCIAS

def MorseCaracterPlano(morse):
    for caracter in EQUIVALENCIAS:
        if EQUIVALENCIAS[caracter] == morse:
            return caracter
    
    return ""

def DecodificarMorse(morse):
    textoPlano = ""

    for caracterMorse in morse.split(" "):
        # Por cada caracter buscamos su equivalencia.
        caracterPlano = MorseCaracterPlano(caracterMorse)
        textoPlano += caracterPlano
    
    return textoPlano

def CaracterPlanoMorse(caracter):
    if caracter in EQUIVALENCIAS:
        return EQUIVALENCIAS[caracter]
    else:
        # Si no existe este valor regresamos una cadena vacía.
        return ""

def CodificarMorse(textoPlano):
    textoPlano = textoPlano.upper() # Mayusculas para evitar hacer mas comparaciones
    morse = "" # Alojamiento del resultado

    for caracter in textoPlano:
        caracterCodificado = CaracterPlanoMorse(caracter) # Por cada carácter, buscamos su equivalencia.
        morse += caracterCodificado + " " # Lo concatenamos al resultado, además de agregar un espacio.

    return morse

palabra = "HOLA"
print("> Codificado: ")
codificado = CodificarMorse(palabra)
print(codificado)
print("> Decodificada: ")
decodificado = DecodificarMorse(codificado)
print(decodificado)