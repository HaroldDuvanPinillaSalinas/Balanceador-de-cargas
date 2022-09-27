import sys
import zmq
from tienda import tienda as tda

class Cliente:

    def __init__(self, cedula, nombres, apellidos, user, password):
        self.cedula = cedula
        self.nombres = nombres
        self.apellidos = apellidos
        self.user = user
        self.password = password

    def conexion(self):
        ip_balanceador = ""
        port = ""
        if len(sys.argv) != 3:
            print("Los argumentos son incorrectos. La estructura es -> <python/py> <nombre_programa.py> <direccion_ip> <puerto>")
        else:
            ip_balanceador = sys.argv[1]
            port = sys.argv[2]
        
        context = zmq.Context()
        print ("Connecting to balancer...")
        socket = context.socket(zmq.REQ)
        socket.connect ("tcp://%s:%s" % (ip_balanceador, port))

        #  Do 10 requests, waiting each time for a response
        for request in range (1,10):
            print ("Sending request ", request,"...")
            socket.send_string("Hello")
            #  Get the reply.
            message = socket.recv()
            print ("Received reply ", request, "[", message, "]")

    def consultar_tienda(self):
        tienda = tda
        print(tienda.imprimir())

client = Cliente(1234, "Harold", "Pinilla", "hp", "1234")
# client.consultar_tienda()
client.conexion()