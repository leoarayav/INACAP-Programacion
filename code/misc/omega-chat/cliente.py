import socket
import threading
from constants import estilo
from colorama import Fore

def mensaje(self, color, mensaje):
    print(color + mensaje + Fore.RESET)

print(estilo.BANNER)
nickname = input("[OMEGA-CHAT | Inicio] Ingresa tu nombre de usuario: ")

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('127.0.0.1', 60655))

def ClienteRecibir(self):
    while True:
        try:
            mensaje = cliente.recv(1024).decode('ascii')

            if mensaje == 'NICK':
                cliente.send(nickname.encode('ascii'))
            else:
                self.mensaje(mensaje)
        except:
            self.mensaje("[OMEGA-CHAT | Error] Ha ocurrido un error dentro del cliente!")
            cliente.close()
            break

def ClienteEscribir(self):
    while True:
        mensaje = f'<{nickname}> {input("")}'
        cliente.send(mensaje.encode('ascii'))


if __name__ == '__main__':
    thread_recibido = threading.Thread(target=ClienteRecibir)
    thread_recibido.start()

    escribir_thread = threading.Thread(target=ClienteEscribir)
    escribir_thread.start()
