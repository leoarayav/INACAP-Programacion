from time import sleep
from webbrowser import open
from colorama import Fore

"""
    Archivo principal del repositorio: "INACAP-Programación"

    Brief:
        - Con este archivo podremos determinar y/o verificar la funcionalidad del repositorio y de los ejercicios agregados.
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
    'N°2',
    'N°3',
    'N°4',
    'N°5',
    'N°6',
    'N°7'
]

URLS = [
    'Actividad 2: https://github.com/leoarayav/INACAP-Programacion/tree/main/code/actividad-2',
    'Actividad 3: https://github.com/leoarayav/INACAP-Programacion/tree/main/code/actividad-3',
    'Actividad 4: https://github.com/leoarayav/INACAP-Programacion/tree/main/code/actividad-4',
    'Actividad 5: https://github.com/leoarayav/INACAP-Programacion/tree/main/code/actividad-5',
    'Actividad 6: https://github.com/leoarayav/INACAP-Programacion/tree/main/code/actividad-6',
    'Actividad 7: https://github.com/leoarayav/INACAP-Programacion/tree/main/code/actividad-7'
]

REPOSITORIO = "https://github.com/leoarayav/INACAP-Programacion"

# Funcionalidad de las actividades e infuncionalidad.
def FuncionalidadCorrecta(actividad: str):
    print(Fore.GREEN, f"[ACTIVIDAD] {actividad} | Funcionalidad: 🟢")

def FuncionalidadIncorrecta(actividad: str):
    Mensaje(Fore.RED, f"[ACTIVIDAD] {actividad} | Funcionalidad: 🔴")

def Mensaje(color, mensaje: str):
    print(color + mensaje + Fore.RESET)

# Lógica del archivo principal.
def ComprobarFuncionalidad(actividad):
    if actividad in ACTIVIDADES:
        FuncionalidadCorrecta(actividad)

    elif actividad not in ACTIVIDADES:
        FuncionalidadIncorrecta(actividad)

    else:
        FuncionalidadIncorrecta(actividad)

def ComprobarActividades():
    actividades = []

    for actividad in ACTIVIDADES:
        sleep(3)
        ComprobarFuncionalidad(actividad)
        
    return actividades

def ListarURLs():
    urls = []

    for url in URLS:
        print(url)
        sleep(3)
    
    return urls

def AccesoRepositorio():
    return open(REPOSITORIO, new = 2, autoraise = True)

def MenuPrincipal():
    MENU = """
    1. Comprobar funcionalidad.
    2. Listar URLs de las actividades.
    3. Acceder al repositorio.
    """

    print(MENU)
    opcion = int(input("Escoge una opcion: "))

    while opcion != 0:
        
        if opcion == 1:
            ComprobarActividades()
            break

        elif opcion == 2:
            ListarURLs()
            break

        elif opcion == 3:
            AccesoRepositorio()
            break

        else:
            Mensaje(Fore.RED, "[ERROR] Opcion invalida. Escogiste una opcion invalida, cerrando el programa por seguridad...")
            sleep(3)
            exit()
    
    return MenuPrincipal()

if __name__ == '__main__':
    MenuPrincipal()