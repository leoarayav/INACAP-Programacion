from time import sleep
from webbrowser import open
from colorama import Fore

"""
    Archivo principal del repositorio: "INACAP-Programación"

    Version:
        Actualmente en la version: 1.0 Release

    Brief:
        - Con este archivo podremos determinar y/o verificar la funcionalidad del repositorio y de los actividads agregados.
        - Podemos utilizarlo para organizar las actividades y los códigos subidos.
        - Se podrá utilizar proximamente la interfaz de comando para el propio repositorio.
    
    Authors:
        - Leo Araya [github.com/le01q] [github.com/leoarayav]
    
    License:
        - MIT License
    
    Copyright:
        INACAP-Programación 2022 (C) - All rights reserved.
"""

ACTIVIDADES = [
    ('Actividad N°2', 'https://github.com/leoarayav/INACAP-Programacion/tree/main/code/actividad-2'),
    ('Actividad N°3', 'https://github.com/leoarayav/INACAP-Programacion/tree/main/code/actividad-3'),
    ('Actividad N°4', 'https://github.com/leoarayav/INACAP-Programacion/tree/main/code/actividad-4'),
    ('Actividad N°5', 'https://github.com/leoarayav/INACAP-Programacion/tree/main/code/actividad-5'),
    ('Actividad N°6', 'https://github.com/leoarayav/INACAP-Programacion/tree/main/code/actividad-6'),
    ('Actividad N°7', 'https://github.com/leoarayav/INACAP-Programacion/tree/main/code/actividad-7')
]

MENU = """
1 - Listar disponibilidad de actividades.
2 - Listar disponibilidad URLs de las actividades.
3 - Descargar actividad completa.
4 - Acceder al repositorio principal.
5 - Salir del programa.
"""

REPOSITORIO = "https://github.com/leoarayav/INACAP-Programacion"

"""
    Lógica del programa a partir de está sección hacia abajo.
"""

def Mensaje(color: Fore, mensaje: str):
    return print(color, mensaje, Fore.RESET)

def ObtenerFuncionalidadActividades(actividad: str):
    if actividad in ACTIVIDADES:
        return Mensaje(Fore.GREEN, f'> {actividad[0]} | 🟢')
    else:
        return Mensaje(Fore.RED, f'> {actividad[0]} | 🔴')

def ObtenerFuncionalidadDirecciones(url: str):
    if url in ACTIVIDADES:
        return Mensaje(Fore.GREEN, f'> {url[1]} | 🟢')
    else:
        return Mensaje(Fore.RED, f'> {url[1]} | 🔴')

def ComprobarActividades():
    for actividad in ACTIVIDADES:
            sleep(2)
            ObtenerFuncionalidadActividades(actividad)

def ComprobarDirecciones():
    for direcciones in ACTIVIDADES:
        sleep(2)
        ObtenerFuncionalidadDirecciones(direcciones)

def MenuPrincipal():
    Mensaje(Fore.WHITE, MENU)
    opcion = int(input("Opcion > "))

    while opcion != 0:
        if opcion == 1:
            ComprobarActividades()
            break

        elif opcion == 2:
            ComprobarDirecciones()
            break

        elif opcion == 3:
            Mensaje(Fore.YELLOW, "Opcion en desarrollo: github.com/leorayav/INACAP-Programacion")
            break

        elif opcion == 4:
            Mensaje(Fore.YELLOW, f"Accediendo a {REPOSITORIO}")
            sleep(2)
            open(REPOSITORIO, new = 2, autoraise = True)
            break
        
        elif opcion == 5:
            Mensaje(Fore.RED, "Saliendo del programa...")
            sleep(2)
            exit()
            
    return MenuPrincipal()

if __name__ == '__main__':
    MenuPrincipal()