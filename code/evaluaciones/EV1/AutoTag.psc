Proceso AutoTag
	Definir tipoCategoria Como Entero;
	Definir tipoTarifa, tarifaNormal, tarifaFinde Como Entero;
	
	Escribir "- - - - - - - - - - - - - - - -";
	Escribir "SISTEMA DE AUTO-TAG";
	Escribir "Selecciona la categoria del vehiculo:";
	Escribir "1. Autos y camionetas";
	Escribir "2. Motos";
	Escribir "3. Camiones  y Buses";
	Escribir "- - - - - - - - - - - - - - - -";
	Escribir "Categoria: ";
	Leer tipoCategoria;
	
	Escribir "Seleccione el tipo de tarifa:";
	Escribir "1. Tarifa NORMAL";
	Escribir "2. Tarifa FIN DE SEMANA";
	Escribir "Opcion: ";
	Leer tipoTarifa;
	
	Segun tipoCategoria Hacer
		1:
			Si tipoTarifa == 1 Entonces
				Escribir "[AUTO-TAG] Seleccionaste la categoria: AUTOS Y CAMIONETAS";
				Escribir "[AUTO-TAG] Tarifa: NORMAL";
				Escribir "[AUTO-TAG] Total a pagar: $2.000";
			SiNo
				Escribir "[AUTO-TAG] Seleccionaste la categoria: AUTOS Y CAMIONETAS";
				Escribir "[AUTO-TAG] Tarifa: FIN DE SEMANA";
				Escribir "[AUTO-TAG] Total a pagar: $3.000";
			FinSi
		2:
			Si tipoTarifa == 1 Entonces
				Escribir "[AUTO-TAG] Seleccionaste la categoria: MOTOS";
				Escribir "[AUTO-TAG] Tarifa: NORMAL";
				Escribir "[AUTO-TAG] Total a pagar: $600";
			SiNo
				Escribir "[AUTO-TAG] Seleccionaste la categoria: MOTOS";
				Escribir "[AUTO-TAG] Tarifa: FIN DE SEMANA";
				Escribir "[AUTO-TAG] Total a pagar: $900";
			FinSi
		3:
			Si tipoTarifa == 1 Entonces
				Escribir "[AUTO-TAG] Seleccionaste la categoria: CAMIONES Y BUSES";
				Escribir "[AUTO-TAG] Tarifa: NORMAL";
				Escribir "[AUTO-TAG] Total a pagar: $3.500";
			SiNo
				Escribir "[AUTO-TAG] Seleccionaste la categoria: CAMIONES Y BUSES";
				Escribir "[AUTO-TAG] Tarifa: FIN DE SEMANA";
				Escribir "[AUTO-TAG] Total a pagar: $5.200";
			FinSi
	FinSegun
	
	Escribir "GRACIAS POR VIAJAR CON AUTOTAG!";
FinProceso