# Práctica 05: Automatización de Configuración de Redes con Python y Telnet

## 1. Objetivo

Desarrollar e implementar un script en Python que permita automatizar la configuración de un router Cisco mediante una conexión Telnet, aplicando conceptos de programación y administración de redes para reducir el tiempo y los errores en tareas de configuración.

---

## 2. Relación con las prácticas anteriores

Esta práctica se relaciona con las actividades realizadas previamente, ya que utiliza la topología creada en GNS3 y los conocimientos adquiridos sobre conectividad, direccionamiento IP y administración de dispositivos de red.

- Práctica 1: Preparación del entorno de trabajo.
- Práctica 2: Configuración de herramientas de automatización.
- Práctica 3: Creación y validación de la topología de red.
- Práctica 4: Introducción a Python y representación de dispositivos de red.
- Práctica 5: Automatización de configuraciones mediante scripts de Python y Telnet.

---

## 3. Topología y direccionamiento utilizados

### Dispositivos utilizados

- NAT Cloud
- Network Automation Container (NAC)
- Ethernet Switch
- Cisco IOSvL2
- Router Cisco IOSv (R1)

### Direccionamiento IP

| Dispositivo | Interfaz | Dirección IP |
|-------------|-----------|-------------|
| NAC | eth0 | Obtenida mediante DHCP |
| R1 | GigabitEthernet0/0 | 192.168.122.70/24 |
| R1 | Loopback0 | 1.1.1.1/32 |
| R1 | Loopback1 | 2.2.2.2/32 |

### Evidencia de la topología

La captura de la topología utilizada se encuentra en la carpeta:

**evidencias/**

---

## 4. Versión de Python utilizada

Para la realización de esta práctica se utilizó Python 3 instalado en el Network Automation Container (NAC).

La evidencia de la versión utilizada se encuentra en la carpeta:

**evidencias/**

---

## 5. Explicación del script

El script desarrollado tiene como finalidad automatizar la configuración del router R1 mediante una conexión Telnet.

Las principales funciones realizadas por el script son:

1. Solicitar las credenciales de acceso.
2. Establecer conexión Telnet con el router.
3. Acceder al modo privilegiado.
4. Ingresar al modo de configuración global.
5. Crear la interfaz Loopback0 con dirección IP 1.1.1.1.
6. Crear la interfaz Loopback1 con dirección IP 2.2.2.2.
7. Configurar el protocolo OSPF.
8. Guardar y finalizar la configuración.

Gracias a este proceso es posible realizar configuraciones de forma automática, reduciendo el tiempo de trabajo y minimizando errores humanos.

---

## 6. Tabla de pruebas

| Prueba realizada | Resultado |
|------------------|------------|
| Obtención de dirección IP mediante DHCP | Exitosa |
| Prueba de conectividad con Ping | Exitosa |
| Acceso Telnet al router | Exitosa |
| Ejecución del script Python | Exitosa |
| Configuración de Loopback0 | Exitosa |
| Configuración de Loopback1 | Exitosa |
| Configuración de OSPF | Exitosa |
| Verificación de interfaces configuradas | Exitosa |

---

## 7. Problemas encontrados y soluciones

| Problema encontrado | Solución aplicada |
|--------------------|------------------|
| El NAC no obtenía dirección IP. | Se verificó la configuración DHCP y se reinició el contenedor. |
| No existía conectividad con el router. | Se comprobó el direccionamiento IP y la conexión entre dispositivos. |
| Error al intentar acceder mediante Telnet. | Se configuraron correctamente las líneas VTY y las credenciales de acceso. |
| Problemas al ingresar al modo privilegiado. | Se configuró correctamente la contraseña enable del router. |

---

## 8. Capturas de evidencia

Todas las capturas solicitadas para la práctica se encuentran almacenadas dentro de la carpeta:

**docs/practica-05/evidencias/**

Las evidencias incluyen:

- Topología en GNS3.
- Dirección IP obtenida mediante DHCP.
- Prueba de conectividad con Ping.
- Acceso Telnet al router.
- Ejecución del script.
- Configuración de Loopback0 y Loopback1.
- Configuración del protocolo OSPF.
- Verificación de la configuración final.

---

## 9. Conclusiones individuales

### Danna Paola Pacheco Marquez:
Durante el desarrollo de esta práctica aprendí a utilizar Python para automatizar configuraciones de 
red mediante una conexión Telnet entre el NAC y un router. Mediante la creación y ejecución de un 
script, logré establecer una conexión remota, acceder al modo privilegiado del router y configurar 
automáticamente las interfaces Loopback 0 y Loopback 1, así como el protocolo de enrutamiento 
OSPF. 
Durante el proceso se me presentaron algunas dificultades, principalmente al intentar establecer la 
conexión Telnet, ya que inicialmente recibía un error de conexión rechazada. Al revisar la 
conectividad mediante el comando ping, pude notar que las direcciones IP de NAC y R1 pertenecían 
a subredes diferentes, así que ajusté la dirección IP de R1 para que coincidiera con la subred de NAC. 
También comprobé la disponibilidad de Python y de la biblioteca telnetlib, y revisé la configuración 
del router para asegurar que permitiera las conexiones Telnet. 
Finalmente, la práctica me ayudó a comprender la importancia de verificar la conectividad y 
configuración de los dispositivos antes de implementar una automatización. 

### Flor Lizbeth Estrada Hernández:
Durante esta práctica aprendí cómo utilizar Python para facilitar la configuración de dispositivos de 
red mediante un script de automatización. También comprendí cómo funciona la comunicación 
Telnet entre el contenedor NAC y el router, así como la importancia de configurar correctamente las 
direcciones IP y los accesos necesarios para establecer una conexión. Uno de los aspectos que 
considero más importantes fue comprobar que las instrucciones escritas en Python realmente se 
aplicaran en el router. Mediante la revisión de las interfaces Loopback y de la configuración OSPF, 
pude identificar la utilidad de verificar los resultados después de ejecutar un script. Esta actividad me 
permitió relacionar los conocimientos de programación con la administración de redes y comprender 
cómo la automatización puede reducir el trabajo manual y facilitar la configuración de los 
dispositivos.

### Alan Jovany Cruz Pérez:
En el desarrollo de esta práctica aprendí a crear y ejecutar un script en Python para realizar 
configuraciones de manera automática en un router Cisco mediante Telnet. Durante el 
procedimiento pude comprender mejor la función de las librerías, el envío de comandos desde 
Python y la manera en que estos se ejecutan en el dispositivo de red. También reforcé mis 
conocimientos sobre la configuración de interfaces, el acceso al modo privilegiado y el protocolo 
OSPF. La comprobación de los resultados mediante los comandos de verificación me permitió 
entender que no basta con ejecutar un programa, sino que también es necesario revisar que los 
cambios se hayan aplicado correctamente. En conclusión, esta práctica fue importante para conocer 
una aplicación real de Python en la automatización de redes y reconocer cómo estas herramientas 
pueden hacer más eficientes las tareas de configuración y administración de infraestructura.
