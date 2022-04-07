Proceso EmpresaSueldo
	definir primerConteo, segundoConteo, x, n como entero;
	definir sueldo, gastos como real;
	
	primerConteo = 0;
	segundoConteo = 0;
	gastos = 0;
	x = 1;
	
	Escribir "Cantidad de empleados:";
	Leer n;
	
	mientras x <= n hacer
		Escribir "Ingrese el sueldo del empleado aqu� abajo:";
		Leer sueldo;
		
		Si sueldo >= 100 y sueldo <= 300 Entonces
			primerConteo = primerConteo + 1;
		SiNo
			segundoConteo = segundoConteo + 1;
		FinSi
		gastos = gastos + sueldo;
		x = x + 1;
	FinMientras
	
	Escribir "> Empleados que cobran entre $100 y $300: ", primerConteo;
	Escribir "> Empleados que cobran mas de $300: ", segundoConteo;
	Escribir "> Gastos total en sueldo: ", gastos;
	
FinProceso
