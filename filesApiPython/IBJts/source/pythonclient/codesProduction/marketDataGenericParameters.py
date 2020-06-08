#!/usr/bin/env python3
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum 
import datetime
import time
import sys

global myList
global app
global var1
global var2
global finalList

import argparse
global myArgsList

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        global myDict
        #myDict = {}
        #myDict ={'68':'0.0','72':'0.0','73':'0.0','75':'0.0','74':'0.0'}
        myDict ={'68':0,'72':0,'73':0,'75':0,'74':0} #Tener Diccionario con 0 por si un dato No viene.
        global contador
        contador = 3

    def processTickLine(self):
        global contador
        print("GENERANDO FICHERO")
        x = datetime.datetime.now()
        print(x.strftime("%x"))
        myDict ['d'] = x.strftime("%x")
        with open(('./DATOS/%s/%s.txt' % (var1,var2)), 'a+') as f:
            f.write("%s,%2.2f,%2.2f,%2.2f,%2.2f,%i" % ((myDict['d']),
                                                    (myDict['68']),
                                                    (myDict['72']),
                                                    (myDict['73']),
                                                    (myDict['75']),
                                                    (myDict['74'])) + '\n')
        print("Pasando Por Contador")
        contador -= 1
        print(contador)
        if contador == 0:
            print("Termine con un contrato de la lista")
            #self.otroContrato()
            self.disconnect()# Manda al codigo a la linea despues de app.run()
        else:
            print("Faltan lineas para terminar")   

    def error(self, reqId, errorCode, errorString):
        print("Error: ",reqId,"  ",errorCode," ",errorString)
        
    def tickPrice(self, reqId ,tickType, price,attrib):
        if tickType == 68:
            myDict['68'] = price
            print(TickTypeEnum.to_str(tickType),"Price:", price)
            if len(myDict) > 4:
                self.processTickLine()
                                         
        if tickType == 72:#Este tickType solo viene cuando cerro el mercado
            myDict['72'] = price
            print(TickTypeEnum.to_str(tickType),"Price:", price)
        
        if tickType == 73:#Este tickType solo viene cuando cerro el mercado
            myDict['73'] = price
            print(TickTypeEnum.to_str(tickType),"Price:", price)
        
        if tickType == 75:#Este tickType solo viene una vez
            myDict['75'] = price
            print(TickTypeEnum.to_str(tickType),"Price:", price)
            if len(myDict) > 4:
                self.processTickLine()
        
    def tickSize(self, reqId, tickType, size):
        if tickType == 74:
            myDict['74'] = size
            print(TickTypeEnum.to_str(tickType), "Size:", size)
            if len(myDict) > 4:
               self.processTickLine() 
           
def main():
    time.sleep(3)
    global finalList
    global myList
    global app
    global var1
    global var2
    app = TestApp()
    app.connect("127.0.0.1", 7497, 0)
    print("serverVersion:%s connectionTime:%s" % (app.serverVersion(),app.twsConnectionTime()))
    
    time.sleep(3)
    contract = Contract()
    contract.symbol = var2                #variable 2
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"
    contract.primaryExchange = var1     #variable 1 

        #Esto son metodos de la clase EClient
    app.reqMarketDataType(4) # Este 4 es para delayed-frozen data
                
                #(tickrId, contract, genericTickList(GenericTickTypes), snapshot, regulatorySnaphsot,mkdDataOptions)
    app.reqMktData(0,contract,"",False,False,[])
    app.run()
    print("Existen mas contratos ???")
    newContrato()#Importante Evalua si existen mas contratos
    
def contratos():
    global myList
    global finalList
    global var1
    global var2
    finalList = [] # Lista Vacia
    myList = []
    print("Todos los contratos")
    with open('descargas.txt','r') as file: 
        # reading each line	 
        for line in file: 
            for word in line.split():
                print(word)
                myList.append(word)
            print("Termine de leer una linea del fichero")
			#print("Lista Previa donde se elimina el EOL:")
        print("Lista donde se elimina el EndOfLine del fichero descargas.txt:")
        print(myList)
        print("Uniendo los elementos en la lista")
        print(','.join(myList))
        s = (','.join(myList))#Juntando todo los elementos en una variable
        print("Valor de S:")
        print(s)
        for elemento in s.split(','):
            print(elemento)
            finalList.append(elemento)
        print("Lista Final para Contratos")
        print(finalList)
        print("Asigno Posicion")	
        var1 = finalList[0]
        var2 = finalList[1]
        print(finalList)
        print("Termine el bucle de for y lectura del archivo.txt / Tengo un array de contratos")
            
def newContrato():
    global app
    global var1
    global var2 
    global myList
    global finalList
    print("Elimine conexion del objeto anterior de la clase TestApp")
    finalList.remove(finalList[0])
    finalList.remove(finalList[0])
    
    if len(finalList) == 0:
        print("Termine todos los contratos")
        sys.exit()
    else:
        print("Faltan contratos")
        print("Asigno posiciones")
    var1 = finalList[0]
    var2 = finalList[1]
    print(finalList)
    main()

def listContratos():
    global myList
    myList = [] # Lista Vacia
    finalList = [] # Lista Vacia

    with open('descargas.txt','r') as file: #Este tiene coma en el texto 
        # reading each line	 
        for line in file:
            for word in line.split():	
                #print(word)
                myList.append(word)
    print("List Financial Instruments Available: ['MARKET,STOCK','MARKET,STOCK','MARKET,STOCK'....] ")
    print(myList)
    #sys.exit()

def downloadsFichero (args):
    print("Funcion descargar instrumentos del Fichero")
    contratos()
    main()
    
def listFichero (args):
    print("Funcion para leer Fichero")
    listContratos()
    sys.exit()

def addFichero (args):
    print("Funcion para agregar instrumentos al Fichero")
    print(var3)
    print(var4)
    global myList
    global myAddList1
    myList = [] # Lista Vacia
    myAddList1 = []#Los datos guardados en esta lista se usaran para escribir en el archivo .txt
    myAddList1.append(var3)
    myAddList1.append(var4)
    print(myAddList1)
    print(myAddList1[0])
    print(myAddList1[1])
    with open('descargas.txt', 'a+') as f:
        f.write('\n'+"%s,%s" % ((myAddList1[0]),(myAddList1[1])))#Momento en el que escribe en el archivo.txt
        
    with open('descargas.txt','r') as file: #Este tiene coma en el texto 
        # reading each line	 
        for line in file:
            for word in line.split():	
                #print(word)
                myList.append(word)
    print("List Financial Instruments Available: ['MARKET,STOCK','MARKET,STOCK','MARKET,STOCK'....] ")
    print(myList)
    print("Se agrego al final del array, el Instrumento Financiero")
    sys.exit()

def delFichero (args):
    global myDelList1
    myDelList1 = []#Los datos guardados en esta lista se usaran para escribir en el archivo .txt
    print(myDelList1)
    print("Funcion para eliminar instrumentos del Fichero")
    with open('descargas.txt','r+') as file: #Este tiene coma en el texto 
        # reading each line	 
        for line in file:
            for word in line.split():
                print(word)
                if word != (var3+","+var4):
                    myDelList1.append(word)#Va colocando los contratos en una lista
                    print(myDelList)
        print("Lista con el contrato eliminado:")
        print(myDelList1)
        print(len(myDelList1))
        contador = len(myDelList1)
    
    with open('descargas.txt','w+') as file:
        print("Inicio contador")
        while (contador != 0):
            file.write(str(myDelList1[0])+'\n')
            myDelList1.remove(myDelList1[0])
            contador -= 1
            print(contador)
            print(myDelList1)
    sys.exit()

parser = argparse.ArgumentParser(description = "Parameters to deply the API IB")#Genero mi objeto

subparsers = parser.add_subparsers(title='Commands Available for the API IB',
                                    description='Each Commands has a diferent function',
                                    dest= 'scmd',
                                    help='Execute each one separate')
                                    #En 'scmd' se guarda el atributo("nombre") de los subcomandos
                                    #Los 'args' son argumentos propios de cada subcomando 
# DOWNLOADS command
downloads_parser = subparsers.add_parser('DOWNLOADS', help='To download all the Financial Instruments')

# LIST command
list_parser = subparsers.add_parser('LIST', help='To list all the Financial Instruments')

# ADD command
adding_parser = subparsers.add_parser('ADD', help='Add Financial Instrument')

adding_parser.add_argument('MARKET', action='store', nargs=1, help='Market name to add')
adding_parser.add_argument('FINANCIAL_INSTRUMENT', action='store', nargs=1, help='Name Instrument')

# DEL command
del_parser = subparsers.add_parser('DEL', help='Deleted Financial Instrument')
del_parser.add_argument('MARKET', action='store', nargs=1, help='Market Name to deleted')
del_parser.add_argument('FINANCIAL_INSTRUMENT', action='store', nargs=1, help='Name Instrument')

args = parser.parse_args()

print(args.scmd)

myAddList = []
myDelList = []
if args.scmd == "DOWNLOADS":##El atributo de args se guarda en el destino 'scmd',se compara y si cumple se ejecuta algo
    downloadsFichero(args)
elif args.scmd == "LIST":
    listFichero(args)
elif args.scmd == "ADD":
    myAddList.append(args.MARKET)##Si mando a imprimir lo que esta dentro de () 
    myAddList.append(args.FINANCIAL_INSTRUMENT)
    print(myAddList)
    var1 = myAddList[0]
    var2 = myAddList[1]
    var3 = var1[0].upper()#Me pone en mayuscula #var3 y var4 seran los datos que se utilizaran en la otra funcion
    var4 = var2[0].upper()#Aqui ya tengo el elemento en un string de caracteres que se llevaran a una lista nueva
    # print(var3)#var3 y var4 seran los datos que se utilizaran en la otra funcion
    # print(var4)
    addFichero(args)
elif args.scmd == "DEL":
    myDelList.append(args.MARKET)
    myDelList.append(args.FINANCIAL_INSTRUMENT)
    print(myDelList)
    var1 = myDelList[0]
    var2 = myDelList[1]
    var3 = var1[0].upper()#Me pone en mayuscula 
    var4 = var2[0].upper()#Aqui ya tengo el elemento en un string de caracteres que se llevaran a una lista nueva
    print(var3)#var3 y var4 seran los datos que se utilizaran en la otra funcion
    print(var4)
    delFichero(args)

print("Debe imprimir valor de args")
print(args)  ##ESTO FUNCIONA--> Devuelve : Namespace(func=<function foo at 0x7fcbac56ed30>)
#print(args.MARKET)##FUNCIONA, PODRIA UTILIZARLO PARA GRABAR DATOS EN UNA LISTA EN CASO SE NECESITE
print("Debio imprimir valor de args")

myArgsList = []
for _, value in parser.parse_args()._get_kwargs():
	if value is not None:
		myArgsList.append(value)
print("PASANDO POR EL FOR y SIGUIENTE LINEA ES LA LISTA DE ARGUMENTOS")
print(myArgsList)
print(len(myArgsList))

#contratos()
#main()
    