palabra = input("Ingresa la palabra: ")

def ContarVocales(palabra):
    contador = 0
    for vocal in palabra:
        if vocal.lower() in "aeiou":
            contador += 1
    return contador

cantidad = ContarVocales(palabra)
print(f"En la palabra {palabra} hay {cantidad} vocales")
