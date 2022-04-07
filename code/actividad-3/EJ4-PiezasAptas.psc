Proceso PiezasAptas
	Definir cantidad, x, n como entero;
	Definir largo como real;
	x = 1;
	cantidad = 0;
	Escribir "Cuantas piezas vas a procesar?: ";
	Leer n;
	Mientras x <= n Hacer
		Escribir "Ingrese la medida o el largo de la pieza: ";
		Leer largo;
		Si largo >= 1.20 y largo <= 1.30 Entonces
			cantidad = cantidad + 1;
		FinSi
		x = x + 1;
	FinMientras
	Escribir "La cantidad de piezas aptas son: ", cantidad;
	Leer cantidad;
FinProceso
