"""
    El Profesor ha decidido bonificar a los alumnos que tengan menos inasistencias al curso:
    Inasistencia Bonificación

    > Mas de 10 0%
    > Más de 7 hasta 10 3%
    > Más de 4 hasta 7 5%
    > 4 o menos 10%

    Debe solicitar al inicio la cantidad de alumnos del curso.

    El programa debe entregar:
        • La nota reajustada de cada alumno

    Además, debe validar:
        • El número de inasistencias debe ser mayor o igual a 0.
        • Las notas son en escala chilena (de 1,0 a 7,0). Considere valores con
        decimales.
"""

BONIFICACION = [
    ('Mas de 10 inasistencias', 0),
    ('Mas de 7 hasta 10 inasistencias', 3),
    ('Mas de 4 hasta 7 inasistencias', 5),
    ('4 o menos inasistencias', 10)
]

cantidad_alumnos = int(input("> Ingrese la cantidad de los alumnos: "))

while cantidad_alumnos:
    nombre_alumno = str(input("> Nombre del alumno: "))
    nota = float(input("> Calificacion: "))
    inasistencias = int(input("> Inasistencias del alumno: "))

    if inasistencias > 10:
        nota = nota * BONIFICACION[0][1]
        print(f"Info: {nombre_alumno}: (Nota reajustada: {nota})")
        break
    
    elif inasistencias > 7:
        porcentaje = nota * BONIFICACION[1][1]
        print(f"Info: {nombre_alumno}: {nota} {porcentaje}%")
        break