import time as tiempo
from requests import request, get
from colorama import Fore as col

"""
    Archivo principal del repositorio: "INACAP-Programación"

    Version:
        Actualmente en la version: 1.1 Release
    
    Authors:
        - Leo Araya [github.com/le01q] [github.com/leoarayav]
    
    License:
        - MIT License
    
    Copyright:
        INACAP-Programación 2022 (C) - All rights reserved.
"""

MENU = """
1 - Listar disponibilidad de actividades.
"""

"""
    # MEJORA 🔧: Se utilizó un mejoramiento para crear las listas y dictarlas.
"""

ListarActividad = dict[str, list[str]]

ACTIVIDADES: ListarActividad = {
    "Actividad 1": ["-", "🔴"],
    "Actividad 2": ["https://github.com/leoarayav/INACAP-Programacion/tree/main/code/actividad-2", "🟢"],
    "Actividad 3": ["https://github.com/leoarayav/INACAP-Programacion/tree/main/code/actividad-3", "🟢"],
    "Actividad 4": ["https://github.com/leoarayav/INACAP-Programacion/tree/main/code/actividad-4", "🟢"],
    "Actividad 5": ["https://github.com/leoarayav/INACAP-Programacion/tree/main/code/actividad-5", "🟢"],
    "Actividad 6": ["https://github.com/leoarayav/INACAP-Programacion/tree/main/code/actividad-6", "🟢"],
    "Actividad 7": ["https://github.com/leoarayav/INACAP-Programacion/tree/main/code/actividad-7", "🟢"],
    "Actividad 8": ["https://github.com/leoarayav/INACAP-Programacion/tree/main/code/actividad-8", "🟢"]
}

"""
    Funciones del programa, algunas funciones fueron modificadas.
"""

def Mensaje(color, mensaje):
    print(color, mensaje, col.RESET)

def ObtenerActividades(lista: ListarActividad):
    for actividad, valor in lista.items():
        tiempo.sleep(3)
        Mensaje(col.WHITE, f"Actividad: {actividad}\nURL: {valor[0]}\nDisponibilidad: {valor[1]}\n")

def MenuInicial():
    Mensaje(col.WHITE, MENU)
    opcion = int(input("> "))

    while opcion != 0:
        if opcion == 1:
            ObtenerActividades(ACTIVIDADES)
            break

MenuInicial()