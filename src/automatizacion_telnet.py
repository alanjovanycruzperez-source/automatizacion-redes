## Script de automatización

El script utilizado durante la práctica fue almacenado en:

src/automatizacion_telnet.py

### Versión de Python

Python 3.8.5

### Ejecución

El script fue ejecutado mediante el comando:

python3 automatizacion_telnet.py

Durante la ejecución se solicitaron las credenciales Telnet para acceder al router Cisco y aplicar automáticamente la configuración de las interfaces Loopback y del protocolo OSPF.

### Problemas encontrados

Inicialmente se presentó el error:

telnet: Unable to connect to remote host: Connection refused

### Solución aplicada

Se revisó la configuración de acceso remoto del router y posteriormente se logró establecer correctamente la conexión Telnet, permitiendo la ejecución del script de automatización.

### Script
import getpass
import telnetlib

HOST = "192.168.42.70"

user = input("Enter your Telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"configure terminal\n")

tn.write(b"interface loopback 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")

tn.write(b"interface loopback 1\n")
tn.write(b"ip address 2.2.2.2 255.255.255.255\n")

tn.write(b"router ospf 1\n")
tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")

tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
