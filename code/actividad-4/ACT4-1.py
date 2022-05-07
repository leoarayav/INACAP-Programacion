'''
Realizar la carga del lado de un cuadrado, mostrar por pantalla el perímetro del mismo (El
perímetro de un cuadrado se calcula multiplicando el valor del lado por cuatro)
'''

lado = int(input("Ingrese el lado del cuadrado: "))

perimetro = lado * 4

mostrar_perimetro = f"El perimetro del lado ingresado es: {perimetro}"

print(mostrar_perimetro)