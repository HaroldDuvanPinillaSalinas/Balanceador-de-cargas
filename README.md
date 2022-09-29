# Balanceador de cargas
Proyecto semestral para el curso de introducción a sistemas distribuidos

## Implementación inicial
Para la implementación inicial del proyecto, se estableció una conexión básica de envío de mensajes entre los componentes *cliente.py* *balanceador.py* y *servidor.py*. 
Para probar el funcionamiento de manera distribuida, se ejecutó el *cliente* en una máquina física con Windows, el *balanceador* en una máquina virtual con Ubuntu y el *servidor* en la misma máquina que el *cliente*.

Para ejecutar los programas en estos sistemas operativos, se instaló la libreria ZeroMQ de Python con los siguiente comandos: 

> ### Windows 10:
>
>> pip install pyzmq
>

> ### Ubuntu 20.4:
>
>> sudo apt-get update
>
>> sudo apt-get install python3-zmq
>

## Ejecución de los programas:

Para ejecutar los componentes de la implementación inicial, se deben ejecutar los siguiente comandos por consola:

### **Cliente**:

> #### **Windows 10**: 
> python cliente.py <<dirección_ip_balanceador>> <<puerto_de_conexion_clientes>>
>
> #### **Ubuntu 20.4**: 
> python3 cliente.py <<dirección_ip_balanceador>> <<puerto_de_conexion_clientes>>
>

### **Balanceador**:

> #### **Windows 10**: 
> python balanceador.py <<dirección_ip_balanceador>> <<puerto_de_conexion_clientes>> <<puerto_de_conexion_servidores>>
>
> #### **Ubuntu 20.4**: 
> python3 balanceador.py <<dirección_ip_balanceador>> <<puerto_de_conexion_clientes>> <<puerto_de_conexion_servidores>>
>

### **Servidor**:

> #### **Windows 10**: 
> python servidor.py <<dirección_ip_balanceador>> <<puerto_de_conexion_servidoresn>>
>
> #### **Ubuntu 20.4**: 
> python3 servidor.py <<dirección_ip_balanceador>> <<puerto_de_conexion_servidores>>
>
