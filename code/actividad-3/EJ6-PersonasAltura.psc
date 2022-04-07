Proceso AlturaPersonas
	definir x, total como entero;
	definir altura, suma como real;
	escribir "Ingresa el total de las personas: ";
	leer total;
	
	x = 1;
	suma = 0;
	
	mientras x <= total hacer
		Escribir "Ingresa la estatura: ";
		Leer altura;
		suma = suma + altura;
		x = x + 1;
	FinMientras
	
	Escribir "El promedio total del numero de personas ingresado es: ", suma / total;
FinProceso
