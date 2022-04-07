Proceso DiezValores
	Definir conteo, suma, val, promedio como entero;
	conteo = 1;
	suma = 0;
	
	mientras conteo <= 10 Hacer
		Escribir "Ingrese un valor numerico: ";
		Leer val;
		suma = suma + val;
		conteo = conteo + 1;
	FinMientras
	promedio = suma / 10;
	
	Escribir "La suma de los 10 numeros ingresados es: ", suma;
	Escribir "PROMEDIO: ", promedio;
FinProceso
