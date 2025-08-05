# PyDSPBook
## Interactive Python Notebooks on Digital Signal Processing (Spanish)

Cuadernos Interactivos en Python en Procesamiento Digital de Señales (DSP)

Universidad del Quindío

Jorge Iván Marín (jorgemarin@uniquindio.edu.co)


### INSTALACIÓN DEL LIBRO INTERACTIVO

Este libro interactivo puede ser descargado o clonado. A continuación, se describen las dos alternativas de instalación del libro y cómo se puede cargar correctamente en Visual Studio Code.

* **Forma de Instalación 1**. Descarga del repositorio dando clic en el botón verde llamado “Code” y posteriormente, de la lista desplegable, de clic en la opción “Download Zip”  y descomprima el archivo Zip en su computador.

* **Forma de Instalación 2**. Si cuenta con un sistema operativo Linux o tiene instalado en Windows el programa GIT (https://git-scm.com/downloads) asegúrese primero crear una carpeta donde alojará el repositorio. Posteriormente abra un terminal y usando el comando “cd” ingrese a la carpeta destino. Por ejemplo, si la carpeta destino es ``/home/pydspbook`` use el comando:

``cd /home/pydspbook``

A continuación, escriba el siguiente comando para iniciar la clonación:

```
git clone https://github.com/jimarinh/PyDSPBook_es
```

### USO DEL LIBRO INTERACTIVO EN VISUAL STUDIO CODE

Una vez haya descargado el repositorio basta con cargar Visual Studio Code, entorno que puede descargar de https://code.visualstudio.com/. Dentro de VS Code seleccione la opción “File” y luego “Open Folder” para seleccionar la carpeta que descomprimió o clonó. Finalmente, de clic en el botón “Seleccionar Carpeta”. 

Si la carga del cuaderno ha sido correcta, deberá ver una estructura de carpetas por secciones y dentro de cada sección los capítulos del libro. 

**_NOTA: Abra los cuadernos de Python usando el método antes descrito a través de Open Folder. No lo haga abriendo cada cuaderno (archivo ipynb) por separado, pues las dependencias no se cargan correctamente._**


Es altamente recomendable para el primer uso de los cuadernos interactivos que abra el Capítulo 1, expandiendo la Sección 1 del libro interactivo, seleccionando el archivo ``cap1_intro.ipynb`` y ejecute el primer recuadro de código dando clic en el botón > . Este proceso se encarga de instalar todas las bibliotecas de Python que usan todos los cuadernos.