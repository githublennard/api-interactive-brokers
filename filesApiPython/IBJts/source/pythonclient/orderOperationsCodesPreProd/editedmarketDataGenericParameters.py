#!/usr/bin/env python3
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum
from ibapi.order import *
from threading import Timer

import threading
import datetime
import time
import sys
import argparse

#Variables de marketDataGenericParameters
global myList
global app
global var1
global var2
global finalList
global myArgsList
global var3
global var4
global var5
global var6

#Variables de OrdenesOperacionesReadProduction
global myOrderList
myOrderList = [] # Lista Vacia
global varoOp #operacion contrato
global varoVoSo #Numero (Volumen de activos o posicion Solicitados en la orden)
global varoMax #Precio Maximo del stock
global varcMer #Mercado #Se tiene que usar ISLAND en vez de "NASDAQ"
global varcSym #Symbol
global statusOrd
global priceOrd
global dictOper #Diccionario para imprimir las ordenes ejecutadas
dictOper = {}

#####################################AQUI COMIENZA LA CLASE DESCARGA DATOS#########################################
class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        global myDict
        myDict ={'68':0,'72':0,'73':0,'75':0,'74':0} #Tener Diccionario con 0 por si un dato No viene.
        global contador
        contador = 3

    def processTickLine(self):
        global contador
        print("GENERANDO FICHERO DATOS FINANCIEROS DE ACCIONES")
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

###############************METODO PARA INSTANCIAR LA CLASE DESCARGA DATOS************################
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
        for line in file: # reading each line
            for word in line.split():
                print(word)
                myList.append(word)
            print("Termine de leer una linea del fichero")

        print("Lista donde se elimina el EndOfLine del fichero descargas.txt:") #print("Lista Previa donde se elimina el EOL:")
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

##################################AQUI COMIENZA LA CLASE ORDENES OPERACIONES##########################################

class OrdersApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)#Esto inicia conexion con los servidores de TWS IB
                    
    def processOperations(self):
        global contador
        print("GENERANDO FICHERO DE OPERACIONES")
        x = datetime.datetime.now()
        print(x.strftime("%x"))
        dictOper ['date'] = x.strftime("%x")
        with open('./operaciones.txt', 'a+') as f: ##En operaciones.txt tendremos 8 columnas 
            f.write("%s,%s,%s,%s,%d,%2.2f,%d,%s" % ((dictOper['date']),
                                                    (dictOper['varoOp']),
                                                    (dictOper['varcMer']),
                                                    (dictOper['varcSym']),
                                                    (dictOper['varoVoFi']),
                                                    (dictOper['priceOrd']),
                                                    (dictOper['varoRe']),
                                                    (dictOper['statusOrd'])) + '\n')
        print("REGISTRE STATUS DE LA ORDEN EJECUTADA POR EL SISTEMA")
        
    #Receives next valid order id. Will be invoked automatically upon successfull API client connection, or after
    #call to EClient::reqIds Important: the next valid order ID is only valid at the time it is received. 
    def nextValidId(self, orderId): #Callback
        self.nextOrderId = orderId
        self.start() #Llama a la funcion de start ##Genera objeto contrato y order##Tengo mis dudas que hace llamando a "start()
        print("ESTOY EN LA FUNCION nextValidId" + '\n')

    def error(self,reqId, errorCode, errorString):
        print("Error:  ",reqId,"  ",errorCode,"  ",errorString)

    def orderStatus(self, orderId, status, filled, remaining, avgFillPrice, permId, parentId, lastFillPrice, clientId, whyHeld, mktCapPrice):
        print('orderStatus  Id:', orderId, 'status:', status, 'filled', filled, 'remaining', remaining, 'lastFillPrice', lastFillPrice)
        dictOper ['statusOrd'] = status
        dictOper ['priceOrd'] = lastFillPrice # precio al cual cerro posicion total o parcial 
        dictOper ['varoVoFi'] = filled #remaining #varoVo #Filled porque es la cantidad a la cual cerro posicion
        dictOper ['varoRe'] = remaining #El volumen que queda pendiente de toda la orden
        print(dictOper ['statusOrd'])
        print(dictOper ['priceOrd'] )
        print(dictOper ['varoVoFi'])
        print(dictOper ['varoRe'])
        self.processOperations()

    def openOrder(self, orderId, contract:Contract, order:Order, orderState):#Revisar los parametros con la documentacion #EWrapper
        print('openOrder Id:', orderId, contract.symbol, contract.secType, '@', contract.exchange, contract.primaryExchange , ':', order.action, order.orderType, order.totalQuantity, orderState.status)
        print("PASANDO POR openOrder" + '\n')
        dictOper ['varoOp'] = order.action #varoOp
        dictOper ['varoMax'] = order.lmtPrice #varoMax
        dictOper ['varcSym'] = contract.symbol #varcSym
        dictOper ['varcMer'] = contract.exchange ##Me muestra ordenes anteriores y la que corre actualmente 
                                                 

    def execDetails(self, reqId, contract, execution):
        print('executedDetails: ', reqId, contract.symbol, contract.secType, contract.currency, execution.execId, execution.orderId, execution.shares, execution.lastLiquidity, execution.price)
        print(execution.price)
        print(contract.exchange)
   
    def start(self):#Esta funcion genera un contrato  y objeto order
        
        print("COLOCANDO DATOS DE LA ORDEN EN LAS VARIABLES GLOBALES: " )    
        
        contract = Contract()
        contract.symbol = varcSym #"AMZN"
        contract.secType = "STK"
        contract.currency = "USD"
        #In the API side, NASDAQ is always defined as ISLAND in the exchange field
        contract.exchange = varcMer #"ISLAND"

        order = Order()
        order.action = varoOp #"BUY" #"SELL"
        order.totalQuantity = varoVoSo #100
        order.orderType = "LMT"
        order.lmtPrice = varoMax #347.02
           
        self.placeOrder(self.nextOrderId,contract,order)#places or modifies an order. #id,contract, order
        
    def stop(self):
        self.done = True
        self.disconnect()
        print("PASANDO POR STOP() Y REGRESA AL MAIN PARA REVISAR SI EXISTE OTRA ORDEN PARA EJECUTAR" + '\n')

###############************METODO PARA INSTANCIAR LA CLASE ORDENES OPERACIONES***********################
def main1():
    time.sleep(3)
    app = OrdersApp()
    app.nextorderId = 0
    app.connect("127.0.0.1", 7497, 0)
    time.sleep(3)
    print("PASANDO POR main1() LUEGO POR app.run()")

    Timer(6, app.stop).start()#Al parecer se ejecuta el start() y el Timer como que espera 6 segundo para ejecutar el stop()
    app.run()
    print("EXISTEN MAS ORDENES ??? SINO EXISTE ORDENES A EJECUTAR LA PROXIMA FUNCION TERMINARA EL PROGRAMA")
    newOrders()##SI NO HAY MAS CONTRATOS REGRESA A LA SIGUIENTE LINEA Y SI HAY LA FUNCION LO MANDARA DIRECTO AL main1()
    ##ESTA FUNCION LUEGO DE EJECUTAR REGRESA A LA SIGUIENTE LINEA Y SI HAY UN CONTRATO PENDIENTE LA FUNCION LO MANDARA DIRECTO AL main1()

def newOrders():
    global app
    global varoOp #operacion contrato
    global varoVoSo #Numero (Volumen de activos o posicion Solicitados en la orden)
    global varoMax #Precio Maximo del stock
    global varcMer #Mercado
    global varcSym #Symbol
    global myOrderList

    print("SE ELIMINO LA CONEXION CON LA PLATAFORMA YA QUE VA DE LA MANO CON OBJETOS CREADO PARA LA CLASE PRINCIPAL TestApp QUE ES GLOBAL"+ '\n')
    print("LISTA CON ORDENES PENDIENTES A EJECUTAR: ")
    print(len(myOrderList))
    print(myOrderList)

    if len(myOrderList) == 0:
        print("TERMINE TODAS LAS ORDENES")
        sys.exit()#ESTO FUNCIONA PERFECTAMENTE PARA SALIR DEL PROGRAMA
    else:
        print("FALTAN ORDENES")
        print("ASIGNARE POSICIONES")
    varoOp = myOrderList[1]#"BUY"
    varoVoSo = myOrderList[4]#150
    varoMax = myOrderList[5]#361.20
    varcSym = myOrderList[3]#"AAPL"
    varcMer = myOrderList[2]#"ISLAND" #Se tiene que usar ISLAND en ves de "NASDAQ"
    print("VOY A ELIMINAR DATOS DE LA ORDEN QUE FUE AGREGADA A LAS VARIABLES, POR LO TANTO LA SIGUIENTE LISTA TENDRA LAS ORDENES PENDIENTES")
    del myOrderList[0:6]
    print(myOrderList)
    main1()

def readOrdenes():
    global varoOp #operacion contrato
    global varoVoSo #Numero (Volumen de activos o posicion Solicitados en la orden)
    global varoMax #Precio Maximo del stock
    global varcMer #Mercado
    global varcSym #Symbol
    global myOrderList ##Ya estaba declarado al inicio del codigo

    with open('ordenes.txt','r') as file:
        for line in file:# reading each line
            for word in line.split():
                #print(word)
                myOrderList.append(word)
        print("LISTA PREVIA: ")
        print(myOrderList)
    print("TENGO UNA LISTA DE TODAS LAS ORDENES A EJECUTAR" + '\n')
    print(len(myOrderList))
    varoOp = myOrderList[1]#"BUY"
    varoVoSo = myOrderList[4]#150
    varoMax = myOrderList[5]#361.20
    varcSym = myOrderList[3]#"AAPL"
    varcMer = myOrderList[2]#"ISLAND" #Se tiene que usar ISLAND en ves de "NASDAQ"
    del myOrderList[0:6] #AQUI YA BORRE 6 DATOS DE LA LISTA
    print(varoOp)
    print(varoVoSo)
    print(varoMax)
    print(varcSym)
    print(varcMer)
    print("LISTA DE ORDENES POR EJECUTAR LUEGO DE LA PRIMERA ORDEN: " + '\n')
    print(len(myOrderList))
    print(myOrderList)

###################################IMPLEMENTACION DE FUNCIONES ARGPARSE | METODOS#######################################################
def listContratos():
    global myList
    myList = [] # Lista Vacia
    finalList = [] # Lista Vacia

    with open('descargas.txt','r') as file: #Este tiene coma en el texto
        for line in file:# reading each line
            for word in line.split():
                #print(word)
                myList.append(word)
    print("List Financial Instruments Available: ['MARKET,STOCK','MARKET,STOCK','MARKET,STOCK'....] ")
    print(myList)

def listOpContratos():
    global myList
    myList = [] # Lista Vacia
    finalList = [] # Lista Vacia

    with open('ordenes.txt','r') as file: #Este tiene coma en el texto
        # reading each line
        for line in file:
            #for word in line.split(" ",2):
            for word in line.split():
                #print(word)
                myList.append(word)
    print("LIST OF ALL ORDERS TO EXECUTE: [ID,OPERATION,MARKET,STOCK,QUANTITY,MAX PRICE]")
    while (len(myList) > 0) :
        print(myList[0:6])#Comienza desde Cero pero no toma el 6
        del myList[0:6]

####################################################DECLARACION FUNCIONES ARGPARSE#####################################################

def downloadsFichero(args):
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

    with open('descargas.txt','r') as file:
        for line in file: # reading each line
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
    with open('descargas.txt','r+') as file: #Leo el fichero y si coincide con lo que quiero eliminar no guardo el dato
        for line in file: # reading each line
            for word in line.split():
                print(word)
                if word != (var3+","+var4):
                    myDelList1.append(word)#Va colocando los contratos en una lista
                    print(myDelList)
        print("Lista con el contrato eliminado:")
        print(myDelList1)
        print(len(myDelList1))
        contador = len(myDelList1)#Este contador se usa en la siguiente funcion

    with open('descargas.txt','w+') as file:
        print("Inicio contador")
        while (contador != 0):
            file.write(str(myDelList1[0])+'\n')
            myDelList1.remove(myDelList1[0])
            contador -= 1
            print(contador)
            print(myDelList1)
    sys.exit()

def listOpFicheros (args):
    #print("Funcion para ver todas ordenes")
    listOpContratos()
    sys.exit()

def addFicheroOp (args):
    myList = [] # Lista Vacia
    print("Funcion para agregar Ordenes al Fichero")
    #print(myAddOpList)
    with open('ordenes.txt', 'a+') as f:
        f.write('\n'+"%d %s %s %s %d %2.2f" %  (int(myAddOpList[0]),
                                                (myAddOpList[1]),
                                                (myAddOpList[2]),
                                                (myAddOpList[3]),
                                                int(myAddOpList[4]),
                                                float(myAddOpList[5])))#Momento en el que escribe en el archivo.txt

    with open('ordenes.txt','r') as file: #Este tiene coma en el texto
        for line in file:# reading each line
            for word in line.split():
                myList.append(word)
    print(len(myList))
    print(myList)
    print("\n")
    print("LIST OF ALL ORDERS AFTER EXECUTED PARAMETER ADDOP: [ID,OPERATION,MARKET,STOCK,QUANTITY,MAX PRICE]"+"\n")
    while (len(myList) > 0) :
        print(myList[0:6])#Comienza desde Cero pero no toma el 6
        del myList[0:6]
    sys.exit()

def delFicheroOp (args):
    global myList
    myList = [] # Lista Vacia
    finalList = [] # Lista Vacia
    finalListAnul = []
    with open('ordenes.txt','r') as file: #Este tiene coma en el texto 
        for line in file:# reading each line	 
            for word in line.split():		
                #print(word)
                myList.append(word)
    #print(myList)
    print("Tamaño Lista")
    print(len(myList))
    print("El dato que se paso por parametro: ")
    print(var3)
    
    while len(myList) > 0 :
        print("Primer elemento de la lista: ")
        print(myList[0])
        if myList[0] != var3 :
            finalList.append(myList[0:6])
            del myList[0:6]
        else:
            del myList[0:6]
            #print("Borro la orden y el tamaño que queda es: ")
            
    print("\n")
    print("Lista con ordenes anuladas: ")
    print(finalList)
    print("Tamaño de la lista contenedora: ")
    print(len(finalList))

    while len(finalList) > 0:
        for elemento in finalList[0]:
            #print("elemento que se va a una lista: ")
            finalListAnul.append(elemento) #elemento que se va a una lista
            #print(elemento)
        del finalList[0]#Eliminamos una lista 

    print("print finalListAnul: ")
    print(finalListAnul)

    file = open('ordenes.txt', 'w+')
    file.close()
    while len(finalListAnul) > 0:
        #print("Funcion para agregar Ordenes al Fichero")
        with open('ordenes.txt', 'a+') as f:
                f.write('\n'+"%d %s %s %s %d %2.2f" %  (int(finalListAnul[0]),
                                                    (finalListAnul[1]),
                                                    (finalListAnul[2]),
                                                    (finalListAnul[3]),
                                                    int(finalListAnul[4]),
                                                    float(finalListAnul[5])))#Momento en el que escribe en el archivo.txt
        del finalListAnul[0:6]

    print("WAS UPDATE ORDER LIST")
    sys.exit()

def executeOrders(args):
    print("Funcion ejecutar ordenes")
    readOrdenes()
    main1()
    sys.exit()
    #contratos()
    #main()

##########################################PARAMETROS DEL CODIGO | FUNCION ARGPARSE##################################################################

parser = argparse.ArgumentParser(description = "Parameters to deply the API IB")#Genero mi objeto

subparsers = parser.add_subparsers(title='Commands Available for the API IB',
                                    description='Each Commands has a diferent function',
                                    dest= 'scmd',
                                    help='Execute each one separate')
                                    #En 'scmd' se guarda el atributo("nombre") de los subcomandos
                                    #Los 'args' son argumentos propios de cada subcomando
# DOWNLOADS command
downloads_parser = subparsers.add_parser('DOWNLOADS', help='To download all the Financial Instruments | Example: DOWNLOADS')

# LIST command
list_parser = subparsers.add_parser('LIST', help='To list all the Financial Instruments | Example: LIST')

# ADD command
adding_parser = subparsers.add_parser('ADD', help='Add Financial Instrument | Example: ADD MARKET STOCK')

adding_parser.add_argument('MARKET', action='store', nargs=1, help='Market name to add')
adding_parser.add_argument('FINANCIAL_INSTRUMENT', action='store', nargs=1, help='Name Instrument')

# DEL command
del_parser = subparsers.add_parser('DEL', help='Deleted Financial Instrument | Example: DEL MARKET STOCK ')
del_parser.add_argument('MARKET', action='store', nargs=1, help='Market Name to deleted')
del_parser.add_argument('FINANCIAL_INSTRUMENT', action='store', nargs=1, help='Name Instrument')

# LISTOP command
listop_parser = subparsers.add_parser('LISTOP', help='To list all the Orders to Execute | Example: LISTOP ')

# ADDOP command
addingop_parser = subparsers.add_parser('ADDOP', help='Add order to be execute | Example: ADDOP ID OPERATION MARKET STOCK QUANTITY MAXPRICE')

addingop_parser.add_argument('ID', action='store', nargs=1, help='Market name to add')
addingop_parser.add_argument('OPERATION', action='store', nargs=1, help='Name Instrument')
addingop_parser.add_argument('MARKET', action='store', nargs=1, help='Market name to add')
addingop_parser.add_argument('STOCK', action='store', nargs=1, help='Name Instrument')
addingop_parser.add_argument('QUANTITY', action='store', nargs=1, help='Market name to add')
addingop_parser.add_argument('MAXPRICE', action='store', nargs=1, help='Name Instrument')

# REMOVEOP command
removeop_parser = subparsers.add_parser('REMOVEOP', help='Deleted Order | Example: REMOVEOP ID')
removeop_parser.add_argument('ID', action='store', nargs=1, help='ID to be deleted')

# EXEOP command
exeop_parser = subparsers.add_parser('EXEOP', help='To execute the orders on TWS | Example: EXEOP')


args = parser.parse_args()

print(args.scmd)

myAddList = []
myDelList = []
myAddOpList = []
myTempList = []
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
elif args.scmd == "LISTOP":
    listOpFicheros(args)
elif args.scmd == "ADDOP":
    myAddList.append(args.ID)#append me agrega el valor al final de la lista
    myAddList.append(args.OPERATION)
    myAddList.append(args.MARKET)
    myAddList.append(args.STOCK)
    myAddList.append(args.QUANTITY)
    myAddList.append(args.MAXPRICE)
    print(myAddList)
    print(len(myAddList))
    for word in myAddList:
        myTempList.append(word)#Uso una Lista Temporal
        varTemp = myTempList[-1]#Siempre el ultimo valor de la lista va para la variable varTemp
        varFin = varTemp[0].upper()#upper() Me pone en mayuscula el dato que paso de la lista#varTemp de cierta manera sigue siendo una lista
        #print(varFin)#varFin solo captura el dato que esta dentro de la lista varTemp
        myAddOpList.append(varFin)
    print("Lista con los datos en Mayuscula")
    print(myAddOpList)#Lista con la orden a agregar a la lista
    addFicheroOp(args)
elif args.scmd == "REMOVEOP":
    myDelList.append(args.ID)
    print(myDelList)
    print("Posicion en cero")
    print(myDelList[0])#Esto es lo mismo que print(args.ID)
    var1 = myDelList[0]
    print(var1)#Esto es lo mismo a imprimir print(myDelList[0])
    var3 = var1[0].upper()#Me pone en mayuscula
    print(var3[0])#var3 es el dato que utilizare en la otra funcion #Es el que contiene el ID value
    delFicheroOp(args)
elif args.scmd == "EXEOP":##El atributo de args se guarda en el destino 'scmd',se compara y si cumple se ejecuta algo
    executeOrders(args)

# readOrdenes()
# main1()
#contratos()
#main()
