import socket
import threading
import sys
from random import choice

# Elegir letra al azar
letra = choice("qwertyuiopasdfghjklzxcvbnm")

# Diccionario de categorías y palabras
tablero = {
    "marca": None,
    "comida": None,
    "lugar": None,
    "animal": None
    # Puedes añadir más categorías aquí
}

# Diccionario para almacenar los bloqueos de cada categoría
bloqueos_categorias = {categoria: threading.Lock() for categoria in tablero}

# Variable para controlar si la partida está activa.
partida_activa = False

# Lista que almacena cada uno de los clientes conectados.
clientes = []

# Lista para almacenar los clientes que han enviado la palabra clave "Go!".
clientes_listos = []

# Función para manejar la conexión de cada cliente
def manejar_cliente(cliente, direccion):
    global partida_activa, clientes
    palabra_clave = ''
    print(f"Conexión establecida con {direccion}")

    while True:
        if palabra_clave != "Go!":
            palabra_clave = cliente.recv(1024).decode("utf-8")
            
            # Añadir cliente a la lista de clientes listos
            if palabra_clave == "Go!":
                clientes_listos.append(cliente)
                print(f"{direccion} está listo para empezar.")

                # Esperar a que todos los jugadores estén listos
                if len(clientes_listos) == len(clientes):
                    partida_activa = True

                    # Enviar mensaje de inicio de partida a todos los clientes
                    for c in clientes:
                        c.send("La partida ha comenzado. ¡Buena suerte!".encode("utf-8"))
                        c.send(f"Rellena el siguiente tablero con la letra {letra}:\n{mostrar_tablero()}".encode("utf-8"))
                    # Iniciar temporizador de 120 segundos
                    temporizador = threading.Timer(120, finalizar_partida)
                    temporizador.start()

        if partida_activa:
            # Recibir la categoría y la palabra del cliente
            categoria = cliente.recv(1024).decode("utf-8")
            categoria = categoria.lower()

            # Sección crítica: Actualizar el tablero
            with threading.Lock():
                
                if categoria in tablero.keys():
                    cliente.send("Correcto".encode("utf-8"))
                    # Verificar si la categoría está bloqueada
                    if bloqueos_categorias[categoria].locked():
                        cliente.send(f"La categoría '{categoria}' está bloqueada, otro jugador está escribiendo en ella.".encode("utf-8"))
                    else:
                        bloqueos_categorias[categoria].acquire()  # Bloquear la categoría

                        palabra = ''
                        cliente.settimeout(5)  # Establecer un timeout de 5 segundos para recibir la palabra
                        try:
                            palabra = cliente.recv(1024).decode("utf-8")
                            palabra = palabra.lower()
                            if not tablero[categoria]:
                                if palabra[0] == letra:
                                    palabra = palabra[0].upper() + palabra[1:]
                                    tablero[categoria] = palabra
                                    _, puerto = cliente.getpeername()
                                    for i in clientes:
                                        i.send(f"Palabra agregada por el jugador con id = {puerto}:\n{mostrar_tablero()}".encode("utf-8"))
                                else:
                                    cliente.send(f"La palabra no empieza por la letra asignada, la letra es {letra}".encode("utf-8"))
                            else:
                                cliente.send("Ya hay una palabra en esa categoría.".encode("utf-8"))
                        except socket.timeout:
                            cliente.send(f"\nTiempo maximo alcanzado.\n{mostrar_tablero()}".encode("utf-8"))  # Si no se recibe ninguna palabra en 5 segundos, no se hace nada
                        finally:
                            cliente.settimeout(None)  # Restablecer el timeout

                        bloqueos_categorias[categoria].release()  # Desbloquear la categoría
                else:
                    cliente.send("Categoría no válida.".encode("utf-8"))

            # Verificar si la partida ha terminado
            if not None in tablero.values():
                ganador()

def mostrar_tablero() -> str:
    out = ""
    for i in tablero.keys():
        if tablero[i] is None:
            out += f"{i}:\n"
        else:
            out += f"{i}: {tablero[i]}\n"
    out += "Ingresa la categoría/palabra: "
    return out

# Función para finalizar la partida cuando se complete el tablero
def ganador():
    global servidor, partida_activa
    print("Felicidades, han completado el tablero.")
    for i in clientes:
        i.send("Felicidades, habeis conseguido completar el tablero.".encode("utf-8"))
        i.close()
    # Cerrar el socket después de la conexión
    servidor.close()
    partida_activa = False

# Función para finalizar la partida cuando se agote el tiempo
def finalizar_partida():
    global servidor, partida_activa
    print("Tiempo agotado. Partida finalizada.")
    for i in clientes:
        i.send("Tiempo agotado. Partida finalizada.".encode("utf-8"))
        i.close()
    # Cerrar el socket después de la conexión
    servidor.close()
    partida_activa = False

# Configuración del servidor

#HOST = '127.0.0.1'
#PUERTO = 5555

HOST = str(sys.argv[1])
PUERTO = int(sys.argv[2])

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PUERTO))
servidor.listen()

print(f"Servidor escuchando en {HOST}:{PUERTO}")

while True:
    # Aceptar nuevas conexiones
    cliente, direccion = servidor.accept()
    # Almacenar el cliente para enviarles a todos el mensaje.
    clientes.append(cliente)
    # Crear un nuevo hilo para manejar al cliente
    hilo_cliente = threading.Thread(target=manejar_cliente, args=(cliente, direccion))
    hilo_cliente.start()
