'''
Realizar un programa que solicite la carga por teclado de dos números, si el primero es mayor
al segundo informar su suma y diferencia, en caso contrario informar el producto y la división
del primero respecto al segundo.
'''

num1 = int(input("> Ingrese el primer numero: "))
num2 = int(input("> Ingrese el segundo numero: "))

# Mostramos la condicion
if num1 > num2:
    sum = num1 + num2
    dif = num1 - num2
    print(f"La SUMA entre {num1} y {num2} es: {sum} | La DIFERENCIA de ambos es: {dif}")
else:
    producto = num1 * num2
    div = num1 / num2
    print(f"El PRODUCTO entre {num1} y {num2} es: {producto} | La DIVISION de ambos es: {div}")