import threading
import socket
import time as t

host = '127.0.0.1'# localhost
puerto = 60655 # puerto

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((host, puerto))
servidor.listen()

clientes = []
nicknames = []

def ChatTransmision(mensaje):
    for cliente in clientes:
        cliente.send(mensaje)

def ChatHandle(cliente):
    while True:
        try:
            mensaje = cliente.recv(1024)
            ChatTransmision(mensaje)
        except:
            indice = clientes.index(cliente)
            clientes.remove(cliente)
            cliente.close()
            nickname = nicknames[indice]
            ChatTransmision(f'[OMEGA-CHAT] {nickname} se ha ido del chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break

def ChatRecibir():
    while True:
        cliente, direccion = servidor.accept()

        print(f"[OMEGA-CHAT-BOT] Conectando con: {str(direccion)}")

        cliente.send('NICK'.encode('ascii'))
        nickname = cliente.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clientes.append(cliente)

        print(f'[OMEGA-CHAT | Servidor] El nickname que se conectó es: <{nickname}>')
        ChatTransmision(f'{nickname} se ha unido al chat correctamente!'.encode('ascii'))

        thread = threading.Thread(target=ChatHandle, args=(cliente,))
        thread.start()

if __name__ == '__main__':
    print("[OMEGA | Servidor] Conectando con el servidor, espera un momento...")
    t.sleep(5)
    print("[OMEGA | Conexion] La conexion fue establecida correctamente.")