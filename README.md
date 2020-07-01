# apiIB

This repository will be for documentation about API Interactive Brokers


## Enlace Fotos Explicacion

1. https://monosnap.com/file/SWsJOeyGlJYFlDzo4aii7PVcs9K6YS
2. https://monosnap.com/file/1vmbbvgWKi2p20ajFm10aV7PqFkLiR
3. https://monosnap.com/file/iyGSrLoyjiq0IxKC4peMzV0dioZyuo
4. https://monosnap.com/file/EL0Y2kctRfHRRQE2NBZhTgg6Mc7LV9
5. https://monosnap.com/file/L6q7UWJMp90cdigiLnBcLRe8IdlqP8


### Note

**Name and Path Framework to Deploy the API IBKR from CommandLine with python3:**
```
* PATH: /filesApiPython/IBJts/source/pythonclient/
* NAME: frameworkApiIbkr.py 
* To get description and how to use, please execute in command line: " ./frameworkApiIbkr.py -h "
```
**Environment to deploy**
* Has account in TWS in order to use the API
* Has the Client API (Trader Workstation) installed on computer
* The Trader Workstation should be running at the moment to execute the Framework
* This code was deploy on Linux environment on bash
* You can run using an IDE or without use an IDE   

**Location in GitHub for Python codes to deploy the API:**
* filesApiPython/IBJts/samples/Python/Testbed   --> This path is for files to run in IDE as PyCharm
* filesApiPython/IBJts/source/pythonclient   --> This path is for files to run in bash

**Important Folders in samples path** 
* Folder codesProductionTFM : Codes to get MarketPrices and  HistoricalData from API
* Folder Cotizaciones: Files ".txt" by market
* Folder Historicos: Files ".txt" by market

**Important Folders in source path** (TFM Code) 
* Folder codesProduction : Codes to get MarketPrices from API | Codes to Deploy the API with parameters | Framework Api IBKR
* Folder DATOS : Files ".txt" by market and Stock

**Important Documents on source path** (TFM Code)
* ordenes.txt : Ordenes que se van a ejecutar.
* operaciones.txt : Estatus de cada una de las ordenes que se ejecutan.
* descargas.txt : Datos de los contratos de los cuales se va a descargar informacion financiera.

**To run the code without use IDE go to: /filesApiPython/IBJts/source/pythonclient**
* Execute "setup.py sdist" on bash

**All Files about this project in:**
* /home/lennard/tfmProyecto