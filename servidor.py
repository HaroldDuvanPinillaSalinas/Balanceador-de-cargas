import time
import zmq
import sys

class Servidor:

    def __init__(self) -> None:
        pass

    def conexion(self):
        ip_balanceador = ""
        port = ""
        if len(sys.argv) != 3:
            print("Los argumentos son incorrectos. La estructura es -> <python/py> <nombre_programa.py> <direccion_ip> <puerto>")
        else:
            ip_balanceador = sys.argv[1]
            port = sys.argv[2]
        
        # Socket para comunicarse con el Balanceador
        context = zmq.Context()
        socket = context.socket(zmq.SUB)
        socket.connect ("tcp://%s:%s" % (ip_balanceador, port))

        # Probando la recepción de los mensajes a través del filtro especificado
        topicfilter = "hola"
        socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

        # Leyendo 5 veces el mensaje enviado por el balanceador 
        for i in range(5): 
            string = socket.recv()
            topic, messagedata = string.split()
            print (i+1, "Topic: ", topic, "\tMensaje: ", messagedata)

server = Servidor()
server.conexion()
    
    
