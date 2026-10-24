# Evaluación de la confiabilidad de los recursos

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

# Análisis de un problema técnico hipotético

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
