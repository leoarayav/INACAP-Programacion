Proceso NotasAlumnos
	Definir mayores, menores, x, nota Como Entero;
	altas = 0;
	bajas = 0;
	x = 1; // Conteo
	
	mientras x <= 10 Hacer
		Escribir "Ingrese la nota:",x,": ";
		Leer nota;
		
		si nota >= 7 entonces
			altas = altas + 1;
		SiNo
			bajas = bajas + 1;
		FinSi
		x = x + 1;
	FinMientras
	
	Escribir "- - - - - - - - - - - - - - - - - - - -";
	Escribir "Las notas mayores a un 7 son: ", altas;
	Escribir "Las notas menores a un 7 son: ", bajas;
	Escribir "- - - - - - - - - - - - - - - - - - - -";
FinProceso
