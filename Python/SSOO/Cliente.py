import socket
import sys
import threading
import time

# Configuración del cliente
#HOST = '127.0.0.1'
#PUERTO = 5555

HOST = str(sys.argv[1])
PUERTO = int(sys.argv[2])

# Función para enviar mensajes al servidor
def enviar_mensaje(socket_cliente, mensaje):
    socket_cliente.send(mensaje.encode("utf-8"))

# Función para recibir mensajes del servidor
def recibir_mensaje(socket_cliente):
    return socket_cliente.recv(1024).decode("utf-8")

# Función para manejar la entrada del usuario y enviarla al servidor
def manejar_entrada(socket_cliente):
    while True:
        if not juego_terminado.is_set():
            categoria = input("Ingresa la categoría/palabra: ")
            enviar_mensaje(socket_cliente, categoria)
            time.sleep(0.5)

# Función principal del cliente
def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PUERTO))
    
    print("Bienvenido al juego de palabras. Espera a que todos los jugadores estén listos.")    

    palabra_clave = input("Cuando estés listo para empezar, escribe 'Go!': ")
    enviar_mensaje(cliente, palabra_clave)
    recibir_mensaje(cliente)
    threading.Thread(target=manejar_entrada, args=(cliente,), daemon=True).start()

    while True:
        mensaje_servidor = recibir_mensaje(cliente)
        print(mensaje_servidor)

        if mensaje_servidor.startswith("Juego terminado"):
            juego_terminado.set()
            break

if __name__ == "__main__":
    juego_terminado = threading.Event()
    main()
