# automatizacion-redes
# Mi estación de automatización de redes

## 1. Datos del equipo
Nombres: 
1.-Alan Jovany Cruz Pérez
2.-Danna Paola Pacheco Marquez
3.-Flor Lizbeth Estrada Hernández

## 2. Propósito de la práctica

Instalar, configurar y verificar diferentes herramientas utilizadas en automatización y administración de redes para crear una estación de trabajo funcional.

## 3. Herramientas instaladas
- Python 3.14.7
- Visual Studio Code
- Git
- GitHub
- Postman
- OpenConnect VPN
- Docker Desktop
- VMware Workstation Pro
- GNS3 GUI
- GNS3 VM

## 4. Configuración realizada
- Instalación de Python y configuración del PATH.
- Instalación de Visual Studio Code.
- Instalación de la extensión Python para VS Code.
- Creación del proyecto automatizacion-redes.
- Creación y activación de un entorno virtual (venv).
- Configuración de Git con nombre y correo electrónico.
- Creación del repositorio en GitHub.
- Instalación y prueba de Postman.
- Instalación y verificación de OpenConnect.
- Instalación de Docker Desktop.
- Instalación de GNS3 GUI.
- Descarga e importación de GNS3 VM en VMware.

## 5. Verificación del entorno
Se verificó el funcionamiento de las herramientas mediante:
- python --version
- git --version
- Ejecución del programa hola_mundo.py
- Activación del entorno virtual
- Apertura correcta de Postman
- Apertura correcta de OpenConnect
- Inicio correcto de Docker Desktop
- Apertura correcta de GNS3 GUI
- Integración de GNS3 VM con VMware

## 6. Estructura del proyecto

automatizacion-redes
│
├── README.md
├── requirements.txt
├── src/
├── tests/
├── data/
└── docs/
│
└── practica-01/
│
├── evidencias/
├── instalacion.md
├── configuracion.md
└── verificacion.md

## 7. Probelmas Encontrados
- Problema 1 
PowerShell no permitía activar el entorno virtual.
Solución: Se utilizó el comando: Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

-Problema 2:
Docker Desktop no detectaba soporte de virtualización.
Solución: Se habilitaron las características de virtualización de Windows y se verificó la configuración del sistema.

-Problema 3:
Los enlaces de descarga de OpenConnect presentaban dificultades.
Solución: Se instaló OpenConnect VPN para Windows y se verificó su funcionamiento.

## 8. Conclusiones
-Alan:
A través de esta práctica fue posible construir una estación de trabajo completa orientada a la automatización de redes, integrando herramientas de programación, control de versiones, virtualización, simulación de redes y prueba de servicios. Cada una de las actividades realizadas permitió adquirir nuevos conocimientos y reforzar conceptos importantes sobre administración de sistemas y redes, como resultado, se obtuvo un entorno funcional y preparado para desarrollar prácticas más avanzadas en el futuro, además de una mejor comprensión de las tecnologías utilizadas actualmente en entornos profesionales.
-Danna:
La realización de esta práctica fue una experiencia muy útil porque me permitió conocer y utilizar diversas herramientas que actualmente son empleadas en el área de tecnologías de la información y redes. Aunque durante el proceso se presentaron algunos problemas de instalación y configuración, fue posible resolverlos mediante investigación y pruebas, lo que ayudó a comprender mejor el funcionamiento de cada aplicación. Gracias a esta práctica pude verificar que todo el entorno de trabajo funciona correctamente y entender cómo cada herramienta cumple una función específica dentro de un proyecto de automatización de redes.
-Flor:
Durante esta práctica logré instalar y configurar correctamente todas las herramientas necesarias para la automatización de redes. Aprendí la importancia de preparar adecuadamente un entorno de trabajo antes de comenzar cualquier proyecto, ya que herramientas como Python, Visual Studio Code, Git, Docker, Postman y GNS3 permiten desarrollar, probar y administrar soluciones de una forma más organizada y profesional. Además, pude comprender mejor el funcionamiento de los entornos virtuales y el uso de repositorios para el control de versiones. Esta actividad me permitió fortalecer mis conocimientos técnicos y desarrollar habilidades que serán de gran utilidad en futuras prácticas y proyectos relacionados con redes y automatización.
