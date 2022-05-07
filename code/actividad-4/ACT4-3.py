'''
Realizar un programa que lea cuatro valores numéricos e informar su suma y promedio.
'''

n1 = int(input("> "))
n2 = int(input("> "))
n3 = int(input("> "))
n4 = int(input("> "))

suma = n1 + n2 + n3 + n4
promedio = suma / 4

print(f"El promedio es {promedio} y la suma de todos los valores es igual a {suma}")