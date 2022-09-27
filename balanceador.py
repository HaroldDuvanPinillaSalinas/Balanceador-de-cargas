import time
from traceback import print_tb
import zmq
import sys

class Balanceador:

    def __init__(self) -> None:
        pass

    def conexion_clients(self):
        ip_balanceador = ""
        port = ""
        if len(sys.argv) != 4:
            print("Los argumentos son incorrectos. Debe ingresar lo siguiente -> <python/py> <nombre_programa.py> <direccion_ip> <puerto_conexion_clientes> <puerto_conexion_servidores>")
        else:
            ip_balanceador = sys.argv[1]
            port = sys.argv[2]
        
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://*:%s" % port)

        for i in range (1, 10):
            #  Wait for next request from client
            message = socket.recv()
            print ("Received request: ", message)
            time.sleep (1)  
            socket.send_string("World from %s" % port)

    def conexion_servers(self):
        ip_balanceador = ""
        port = ""
        if len(sys.argv) != 4:
            print("Los argumentos son incorrectos. Debe ingresar lo siguiente -> <python/py> <nombre_programa.py> <direccion_ip> <puerto_conexion_clientes> <puerto_conexion_servidores>")
        else:
            ip_balanceador = sys.argv[1]
            port = sys.argv[3]

        context = zmq.Context()
        socket = context.socket(zmq.PUB)
        socket.bind("tcp://*:%s" % port)

        for i in range (1, 10):
            # Mensaje n°1
            topic = "hola"
            mensaje = "Hola..."
            print("%s %s" % (topic, mensaje))
            socket.send_string("%s %s" % (topic, mensaje))
            time.sleep(1)

            # # Mensaje n°2
            topic = "mundo"
            mensaje = "Mundo..."
            print("%s %s" % (topic, mensaje))
            socket.send_string("%s %s" % (topic, mensaje))
            time.sleep(1)

balanceador = Balanceador()
balanceador.conexion_clients()
balanceador.conexion_servers()

    