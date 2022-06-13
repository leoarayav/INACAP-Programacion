import requests as req
from webbrowser import open
from colorama import Fore
from .constantes import ACTIVIDADES

"""
    Archivo principal
"""

class Principal:
    def __init__(self, actividades: chr = [...]) -> None:
        self.actividades = actividades = ACTIVIDADES
    
    def VerificacionActividades(self) -> chr:
        TODO: ...
    
    def AccesoRepositorio(self) -> None:
        TODO: ...
    
    def VerificarActividad(self) -> None:
        TODO: ...
    
    def MenuInicial(self) -> None:
        TODO: ...
    
    def IniciarPrograma(self) -> None:
        TODO: ...

if __name__ == '__main__':
    principal = Principal()
    principal.IniciarPrograma()