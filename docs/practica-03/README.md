# Práctica 03: Primer programa de Python para representar información de dispositivos 
## 1. Propósito
El objetivo de esta práctica fue desarrollar un programa en Python capaz de representar información básica de dispositivos de red utilizados en una infraestructura simulada. Durante el desarrollo se utilizaron variables, diccionarios, listas, estructuras de control y funciones para almacenar, organizar y mostrar datos relacionados con routers y switches. Esta práctica representa el primer acercamiento al uso de Python para el procesamiento de información de infraestructura de red, sentando las bases para futuras actividades de automatización.

## 2. Conceptos utilizados
- Variables:
Permiten almacenar información dentro del programa, como el nombre, dirección IP o estado de un dispositivo.

- Tipos de datos
Se utilizaron principalmente cadenas de texto (string), listas (list) y diccionarios (dict).

- print()
Se empleó para mostrar información en pantalla de manera organizada.

- Diccionarios
Permitieron agrupar todos los datos relacionados con un dispositivo de red mediante pares clave-valor.

- Listas
Se utilizaron para almacenar varios dispositivos dentro de una misma estructura.

- Ciclo for
Permitió recorrer la lista de dispositivos y mostrar la información de cada uno de ellos.

- Condicional if
Se empleó para verificar el estado de cada dispositivo y determinar si se encontraba activo o fuera de servicio.

- Funciones
Se creó una función para reutilizar código y mostrar la información de los dispositivos de forma más eficiente.

## 3. Dispositivos representados
- R1 - ROUTER - Dirección IP: 10.1.1.1 - Estado: Activo - Función: Enrutamiento
- R2 - ROUTER - Dirección IP: 10.1.1.2 - Estado: Activo - Función: Enrutamiento
- S1 - SWITCH - Dirección IP: 10.1.1.2 - Estado: Activo - Función: Conectividad

## 4. Evidencias
Están dentro de la carpeta de evidencias de practica-03.

## 5. Problemas y soluciones.
- *1.- Problema:* Condición if-else	- *Causa:* Mal escritura de variable, no identificada	- *Solución:* Corrección a la correcta escritura de la variable.
- *2.- Problema:* Estructura en GNS3	- *Causa:* Consola congelada al momento de bootear SO de dispositivos	- *Solución:* Creación de una nueva estructura y configuración desde 0 de la misma.
