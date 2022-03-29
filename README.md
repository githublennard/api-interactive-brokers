# English Version Instructions
# Api Interactive Brokers

This repository will be for documentation about API Interactive Brokers in order to Develop Self-Acting Investment Framework.

This project refers to the Final Master's Project at UC3M (Master in Technologies in the Financial Sector) Course 2019-2020.

## Link Pictures Instructions:

1. https://monosnap.com/file/SWsJOeyGlJYFlDzo4aii7PVcs9K6YS
2. https://monosnap.com/file/1vmbbvgWKi2p20ajFm10aV7PqFkLiR
3. https://monosnap.com/file/iyGSrLoyjiq0IxKC4peMzV0dioZyuo
4. https://monosnap.com/file/EL0Y2kctRfHRRQE2NBZhTgg6Mc7LV9
5. https://monosnap.com/file/L6q7UWJMp90cdigiLnBcLRe8IdlqP8

## Description of Project:

**Name and Path Framework to Deploy the API IBKR from CommandLine with python:**
```
* PATH: /filesApiPython/IBJts/source/pythonclient/
* NAME: frameworkApiIbkr.py 
* To get description and how to use, please execute in command line: "./frameworkApiIbkr.py -h"
```

**Environment work to deploy the project**
* Has account in Interactive Brokers in order to use the API.
* Has the Client API (Trader Workstation / TWS) installed on computer.
* The Trader Workstation should be running at the moment to execute the Framework.
* This code was deploy on Linux environment on bash | On Windows environment it is similary.
* Has installed Python  version >= 3.1
* You can run using an IDE or without use an IDE.

**Location on GitHub and Python codes to deploy the API:**
* filesApiPython/IBJts/samples/Python/Testbed   --> This path is for files to run in IDE as PyCharm
* filesApiPython/IBJts/source/pythonclient   --> This path is for files to run in bash(Command Line)

**Important Folders in path: "filesApiPython/IBJts/samples/Python/Testbed"** 
* Folder codesProductionTFM: Codes to get MarketPrices and  HistoricalData from API.
* Folder Cotizaciones: Files ".txt" by Market.
* Folder Historicos: Files ".txt" by Market.

**Important Folders in path: "filesApiPython/IBJts/source/pythonclient"** (TFM Code) 
```
Folder codesProduction: Framework Api IBKR | Codes to get MarketPrices from API | Codes to Deploy the API with parameters

Folder DATOS: Files ".txt" by Market and Stock.
```

**Important Files in path: "filesApiPython/IBJts/source/pythonclient"** (TFM Code)
* ordenes.txt: File that has all the Market Orders in order to be execute.
* operaciones.txt: File that has Status/Result about each Market Order that was execute.
* descargas.txt: File that has a list all the Financial Instruments to be download in order to get MarketPrices.

**To run the code (Linux environment) without use IDE go to: "/filesApiPython/IBJts/source/pythonclient" and execute:**
* Execute: "setup.py sdist" on bash.
* After the executions, will be available execute all python files from command line.

**All Files about this project in:**
* /home/lennard/tfmProyecto
```
```

# Instrucciones Version en Español
# Api Interactive Brokers

Este repositirio contiene toda la documentacion de la API de Interactive Brokers para el Desarrollo del Framework de Inversion Automatica.

Este proyecto es referente al Trabajo Fin de Máster en la UC3M (Máster en Tecnologías del Sector Financiero) Curso 2019-2020.

## Enlace Fotos Instrucciones:

1. https://monosnap.com/file/SWsJOeyGlJYFlDzo4aii7PVcs9K6YS
2. https://monosnap.com/file/1vmbbvgWKi2p20ajFm10aV7PqFkLiR
3. https://monosnap.com/file/iyGSrLoyjiq0IxKC4peMzV0dioZyuo
4. https://monosnap.com/file/EL0Y2kctRfHRRQE2NBZhTgg6Mc7LV9
5. https://monosnap.com/file/L6q7UWJMp90cdigiLnBcLRe8IdlqP8

### Descripcion del Proyecto:

**Nombre y Ruta del Framework en el directorio, desde donde se puede desplegar a traves de la linea de comandos con python:**
```
* Ruta: /filesApiPython/IBJts/source/pythonclient/
* Nombre: frameworkApiIbkr.py 
* Para obtener ayuda de como desplegar el Framework ejecutar en la linea de comandos: " ./frameworkApiIbkr.py -h "
```

**Entorno de Trabajo para desplegar el proyecto**
* Tener una cuenta en Interactive Brokers para poder usar la API. 
* Instalar el cliente de la API (Trader Workstation / TWS) en el ordenador.
* Debe estar en ejecucion el cliente de la API (Trader Workstation) al momento que se ejecuta el Framework.
* Este proyecto se despliega en Linux desde la linea de comandos | En Windows el procedimiento es similar.
* Tener instalada la version de Python >= 3.1
* Se puede ejecutar usando un IDE o sin usar un IDE.   

**Ruta de los archivos en GitHub y los codigo en Python para poder desplegar el proyecto:**
* filesApiPython/IBJts/samples/Python/Testbed   --> Esta ruta es para ejecutar desde el IDE (PyCharm)
* filesApiPython/IBJts/source/pythonclient   --> Esta ruta es para ejecutar desde la consola

**Carpetas importantes en la ruta: "filesApiPython/IBJts/samples/Python/Testbed"** 
* Carpeta codesProductionTFM: Codigos para obtener "MarketPrices" y "HistoricalData" desde la API.
* Carpeta Cotizaciones: Ficheros con datos de tipo ".txt" y ordenados por mercado.
* Carpeta Historicos: Ficheros de tipo ".txt" y ordenados por mercado.

**Carpetas importantes en la ruta "filesApiPython/IBJts/source/pythonclient"** (TFM Code) 
```
Carpeta "codesProduction": Framework Api IBKR | Codigos para obtener "MarketPrices" desde la API | Codigos para desplegar la API con parametros

Carpeta "DATOS": Ficheros ".txt" organizados por "Market" y "Stock".
```

**Ficheros Importantes en la ruta "filesApiPython/IBJts/source/pythonclient"** (TFM Code)
* ordenes.txt: Fichero con la lista de las ordenes que son para ejecutar.
* operaciones.txt: Fichero que tiene el Estatus/Resultado de cada una de las ordenes que se ejecutaron.
* descargas.txt: Fichero con la lista de los Instrumentos Financieros a descargar para obtener los "MarketPrices".

**Para ejecutar el proyecto (Linux) sin usar un IDE, ir a la siguiente ruta: "/filesApiPython/IBJts/source/pythonclient" y ejecutar:**
* Ejecutar: "setup.py sdist" en la linea comandos.
* Despues de ejecutar la instruccion anterior, se tiene el entorno para la ejecutar los ficheros de python desde la linea de comando.

**Toda la documentacion del proyecto esta en:**
* /home/lennard/tfmProyecto
