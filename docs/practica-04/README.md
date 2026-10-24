
# 1. Propósito de la práctica

El propósito de esta práctica fue identificar, analizar y documentar recursos técnicos confiables relacionados con Python, GNS3 y la automatización de redes. Además, se buscó desarrollar la capacidad de localizar información útil, evaluar su confiabilidad y utilizar comunidades de colaboración para resolver problemas técnicos durante el desarrollo de software.

# 2. Relación con el proyecto integrador

Esta práctica se relaciona directamente con el proyecto integrador, ya que proporciona herramientas y recursos que pueden utilizarse para resolver dudas, corregir errores y desarrollar soluciones durante la creación de programas de automatización de redes. La información recopilada servirá como base de conocimiento para futuras prácticas y facilitará el mantenimiento y mejora de los scripts desarrollados por el equipo.

# 3. Registro de Recursos

## Recursos de Python

### Recurso 1

**Nombre del recurso:** El tutorial de Python (Documentación Python)

**URL:** [Documentación Oficial de Python](https://docs.python.org/es/3/tutorial/)

**Tema que aborda:** Fundamentos de Python y estructuras de programación.

**Tipo de información que ofrece:** Tutoriales, explicaciones y ejemplos sobre variables, listas, diccionarios, ciclos, funciones, módulos y manejo de errores.

**Utilidad para el proyecto integrador:** Permite consultar la sintaxis y los conceptos básicos de Python necesarios para desarrollar scripts orientados a la automatización y administración de redes.

**Ejemplo de una situación en la que se consultaría:** Cuando sea necesario corregir o implementar un ciclo `for` para recorrer una lista de dispositivos de red y mostrar su información de manera automática.


### Recurso 2

**Nombre del recurso:** Guía para desarrolladores de Python

**URL:** [Python Developer's Guide](https://devguide.python.org/)

**Tema que aborda:** Desarrollo, mantenimiento y contribución al lenguaje de programación Python.

**Tipo de información que ofrece:** Guías técnicas sobre configuración del entorno de desarrollo, uso de Git, pruebas de código, documentación y colaboración en proyectos de software.

## Recursos de Redes y Automatización
### Recurso 1

**Nombre del recurso:** Documentación oficial de GNS3

**URL:** [Documentación Oficial de GNS3](https://docs.gns3.com/docs)

**Tema que aborda:** Simulación, configuración y solución de problemas en redes.

**Tipo de información que ofrece:** Guías de instalación, configuración, creación de topologías, uso de dispositivos virtuales y solución de problemas.

**Utilidad para el proyecto integrador:** Permite construir y probar topologías de red en un entorno virtual antes de trabajar con equipos físicos.

**Ejemplo de una situación en la que se consultaría:** Cuando sea necesario solucionar un problema de conexión entre dos routers dentro de una topología de GNS3.

---

### Recurso 2

**Nombre del recurso:** Cisco DevNet

**URL:** [Cisco DevNet](https://developer.cisco.com/)

**Tema que aborda:** Programabilidad, automatización y administración de redes Cisco.

**Tipo de información que ofrece:** Documentación de API, laboratorios prácticos, ejemplos de código, entornos de prueba y recursos de automatización con Python.

**Utilidad para el proyecto integrador:** Permite aprender a interactuar con dispositivos y plataformas de red mediante herramientas de programación y automatización.

**Ejemplo de una situación en la que se consultaría:** Cuando sea necesario aprender a utilizar Python para consultar información de un dispositivo Cisco mediante una interfaz de programación compatible.

---

### Recurso 3

**Nombre del recurso:** Netmiko

**URL:** [Netmiko](https://netmiko.org/)

**Tema que aborda:** Automatización de dispositivos de red mediante Python y conexiones SSH.

**Tipo de información que ofrece:** Instrucciones de instalación, ejemplos de código, documentación y detalles sobre las plataformas compatibles.

**Utilidad para el proyecto integrador:** Permite desarrollar scripts para conectarse a dispositivos compatibles, ejecutar comandos y automatizar tareas de configuración.

**Ejemplo de una situación en la que se consultaría:** Cuando sea necesario crear un script en Python que se conecte a un router y ejecute comandos para consultar o administrar su configuración.

### Nota: Antes de utilizar Netmiko, es necesario verificar la compatibilidad del dispositivo y contar con la autorización correspondiente para acceder a él.

# 4. Evaluación de la confiabilidad de los recursos

| Criterio | Recurso 1: Documentación de Python | Recurso 2: Documentación de GNS3 | Recurso 3: Netmiko |
|-----------|-----------------------------------|----------------------------------|--------------------|
| ¿Quién publica o mantiene el recurso? | La Python Software Foundation y la comunidad oficial de Python. | El equipo de desarrollo de GNS3. | Los desarrolladores y colaboradores del proyecto Netmiko. |
| ¿La información corresponde al tema investigado? | Sí, aborda directamente la programación en Python y sus fundamentos. | Sí, se enfoca en la instalación, configuración y uso de GNS3. | Sí, trata sobre la automatización de dispositivos de red mediante Python. |
| ¿Incluye ejemplos o instrucciones verificables? | Sí, contiene ejemplos de código y ejercicios prácticos. | Sí, proporciona guías, procedimientos y ejemplos de configuración. | Sí, incluye ejemplos de instalación y uso de scripts para conexiones SSH. |
| ¿Se identifica la versión o fecha de actualización cuando corresponde? | Sí, la documentación está organizada por versiones de Python. | Sí, se especifican versiones y actualizaciones de la plataforma. | Sí, se documentan versiones y cambios relevantes del proyecto. |
| ¿Es posible comprobar la información con otra fuente? | Sí, mediante libros, tutoriales y otras referencias oficiales de Python. | Sí, mediante la comunidad de GNS3 y otras fuentes de redes. | Sí, mediante documentación de automatización de redes y ejemplos prácticos. |
| ¿Qué utilidad tiene para el proyecto integrador? | Permite desarrollar scripts en Python para la automatización de tareas. | Ayuda a diseñar y probar topologías de red en un entorno virtual. | Permite automatizar tareas y consultar información de dispositivos de red mediante SSH. |

### ¿Cuál de los recursos consideras más útil para resolver dudas de Python? ¿Por qué?

La documentación oficial de Python es el recurso más útil porque contiene información confiable, actualizada y ejemplos prácticos sobre la sintaxis, funciones y herramientas del lenguaje. Además, es la referencia oficial utilizada por la comunidad de desarrolladores.

### ¿Cuál consultarías para resolver un problema relacionado con GNS3?

Consultaría principalmente la documentación oficial de GNS3, ya que proporciona guías detalladas para la instalación, configuración de topologías, solución de errores y administración de entornos virtuales de red.

### ¿Por qué no conviene copiar directamente una solución sin comprobar que funciona en el entorno de trabajo?

Porque cada entorno puede tener configuraciones, versiones de software o condiciones diferentes. Una solución que funciona para otra persona podría generar errores o no ser compatible con nuestro proyecto. Es importante comprender la solución, probarla y verificar que se adapte a las necesidades del entorno de trabajo.

# 5. Análisis de un problema técnico hipotético

## Situación planteada

El programa `dispositivos.py`, desarrollado en la Práctica 3, muestra correctamente la información de **R1** y **R2**. Sin embargo, al intentar buscar un dispositivo por su nombre, el programa no identifica el equipo solicitado.

Para encontrar una posible solución, se propone investigar el problema mediante la documentación oficial de Python y las comunidades de colaboración, revisando el código y comprobando los resultados antes de realizar cambios.

## Estrategia de solución

| Elemento | Respuesta del equipo |
|-----------|---------------------|
| **Problema identificado** | El programa no encuentra un dispositivo cuando se busca por su nombre, aunque muestra correctamente la información de R1 y R2. |
| **Palabras clave para realizar la búsqueda** | Python, búsqueda por nombre, listas, diccionarios, comparación de cadenas y errores en búsquedas. |
| **Documentación o comunidad que consultarían primero** | Primero se consultaría la documentación oficial de Python para revisar el funcionamiento de listas, diccionarios y comparaciones. Posteriormente, se buscarían casos similares en Stack Overflow en Español. |
| **Información que revisarían en el código** | Se analizaría cómo se almacenan los nombres de los dispositivos, cómo se realiza la búsqueda y si existen errores en las condiciones de comparación o en el acceso a los datos. |
| **Tipo de ejemplo o solución que buscarían** | Ejemplos de código en Python que permitan recorrer listas o diccionarios y localizar un dispositivo mediante su nombre. |
| **Cómo comprobarían que la solución funciona** | Se realizarían pruebas con los nombres de R1 y R2, además de utilizar un nombre inexistente para verificar que el programa encuentra correctamente los dispositivos y maneja adecuadamente los casos sin resultados. |
| **Cómo documentarían la solución encontrada** | Se registraría en el archivo `README.md` el problema identificado, la causa encontrada, la solución aplicada y los resultados obtenidos. Además, los cambios se guardarían en GitHub para que todos los integrantes del equipo puedan consultarlos. |


Esta estrategia permite investigar el problema de manera ordenada, utilizando fuentes confiables y verificando el funcionamiento del código antes de realizar modificaciones. De esta forma, es posible identificar una solución adecuada, documentarla correctamente y conservarla como referencia para futuras prácticas y proyectos de automatización de redes.

# 6. Aprendizajes obtenidos

Durante esta práctica se aprendió la importancia de utilizar fuentes confiables de información para resolver problemas técnicos y ampliar conocimientos sobre programación y redes. También se identificaron recursos especializados en Python, GNS3 y automatización de infraestructura digital que pueden consultarse en futuras actividades. Además, se comprendió la utilidad de las comunidades de colaboración para encontrar soluciones, compartir experiencias y aprender de otros usuarios. Finalmente, se reforzó la importancia de documentar los hallazgos obtenidos para facilitar el trabajo en equipo y la reutilización del conocimiento en el proyecto integrador.

# 7. Conclusiones individuales

## Danna Pacheco

En esta práctica aprendí que la documentación oficial proporciona información técnica confiable sobre el uso de herramientas y lenguajes de programación, mientras que las comunidades ofrecen respuestas y experiencias compartidas por otros usuarios. Para determinar si un recurso es confiable, revisaría quién lo publicó, su fecha de actualización, la claridad de la información y si sus ejemplos funcionan correctamente. Una comunidad como Stack Overflow me ayudaría a resolver problemas de Python mediante preguntas y respuestas de personas que han enfrentado dificultades similares. 
También comprendí que es importante documentar las soluciones encontradas en GitHub, ya que esto permite guardar los avances, consultar los cambios realizados y compartir conocimientos con el equipo, además, facilita identificar errores y reutilizar soluciones en futuras actividades. En las siguientes prácticas del proyecto integrador puedo utilizar la documentación oficial de Python para consultar instrucciones y ejemplos de código, así como los recursos de GNS3 y Cisco DevNet para resolver dudas relacionadas con redes. También, como ya lo hemos estado haciendo desde las prácticas pasadas, usaremos GitHub para organizar los archivos y colaborar como equipo. 


## Alan Cruz

Durante esta práctica comprendí que la documentación oficial permite conocer de manera detallada cómo funcionan los lenguajes y las herramientas tecnológicas, mientras que las comunidades ayudan a encontrar soluciones a partir de las experiencias de otras personas. Para saber si una fuente es confiable, tomaría en cuenta que provenga de un sitio reconocido, que la información esté actualizada y que los ejemplos sean correctos. Si tuviera un problema con un programa de Python, podría consultar Stack Overflow para encontrar casos similares y revisar las posibles soluciones. 
Además, utilizaría GitHub para registrar las correcciones y guardar los cambios realizados en el código, de modo que el equipo pueda consultarlos posteriormente, como ya hemos estado trabajando en el repositorio creado. Esto ayudaría a mantener un mejor control del proyecto y evitar repetir errores. En las próximas prácticas, consultaría la documentación de Python para mejorar mis programas y utilizaría GNS3 y Cisco DevNet para aprender más sobre la configuración y automatización de redes. También, compartiría los avances con mis compañeros mediante GitHub. Considero que aprender a utilizar estos recursos es importante para resolver dificultades y desarrollar proyectos tecnológicos de mejor calidad.

## Flor Estrada

Esta actividad me permitió identificar la importancia de consultar diferentes fuentes de información cuando se trabaja con programación y redes. La documentación oficial contiene instrucciones y explicaciones elaboradas por los responsables de una herramienta, mientras que las comunidades permiten intercambiar ideas, plantear dudas y conocer distintas formas de solucionar un problema. Para elegir un recurso adecuado, verificaría la autoridad del autor, la actualidad de los datos, la existencia de ejemplos y la posibilidad de comprobar los resultados. En caso de tener un error en Python, podría buscar el mensaje que aparece en pantalla dentro de una comunidad y comparar las respuestas con la documentación oficial antes de aplicar una solución. 
Por otro lado, GitHub permite conservar el historial de modificaciones, compartir el código y registrar las soluciones que funcionan. Esto es muy útil porque así todos los integrantes del equipo pueden conocer los avances y continuar el trabajo de otros compañeros. En las siguientes prácticas del proyecto integrador, utilizaremos estos recursos para investigar dudas, mejorar mis scripts, solucionar problemas de conectividad en GNS3 y aprender técnicas de automatización. De esta manera, podremos trabajar de forma más organizada, independiente y colaborativa.
