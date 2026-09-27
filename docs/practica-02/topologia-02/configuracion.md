# Configuración de la Topología 2
 
Se creó una red en GNS3 utilizando dos routers Cisco IOSv y un switch multicapa Cisco IOSvL2.
 
## R1
 
- GigabitEthernet0/0: 10.1.1.1/24
- Loopback0: 1.1.1.1/32
 
## R2
 
- GigabitEthernet0/0: 10.1.1.2/24
- Loopback0: 2.2.2.2/32
 
## S1
 
- VLAN 1: 10.1.1.3/24
 
## OSPF
 
Se configuró el protocolo OSPF proceso 1 en R1 y R2 utilizando el área 0.
 
Se realizaron pruebas de conectividad entre R1 y R2. También se verificó el funcionamiento de OSPF mediante el comando:
 
show ip ospf neighbor
 
Finalmente, se utilizó:
 
show ip route
 
para comprobar las redes conectadas y las rutas aprendidas mediante OSPF.
 
Los resultados demostraron que la topología funciona correctamente y que los routers pueden intercambiar información de enrutamiento mediante OSPF.
