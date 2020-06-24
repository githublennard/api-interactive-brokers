from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import *
from threading import Timer

import threading
import time
import datetime

global varoOp #operacion contrato
global varoVo #Nummero (Volumen de activos o posicion)
global varoMax #Precio Maximo del stock
global varcMer #Mercado
global varcSym #Symbol
global statusOrd
global priceOrd
global dictOper
dictOper = {}

varoOp = "BUY"
varoVo = 100
varoMax = 364.19
varcSym = "AAPL"
varcMer = "NASDAQ"

# dictOper ['varoOp'] = varoOp
# dictOper ['varoVo'] = varoVo #filled de orderStatus
# dictOper ['varoMax'] = varoMax
# dictOper ['varcSym'] = varcSym
# dictOper ['varcMer'] = varcMer
# dictOper ['varoRe'] = varoRe #remaining, lo que queda pendiente por cerrar en el contrato
class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)#Esto inicia conexion con los servidores de TWS IB
        #global dictOper
        #dictOper = {}
    
    def processOperations(self):
        print("GENERANDO FICHERO DE OPERACIONES")
        x = datetime.datetime.now()
        print(x.strftime("%x"))
        dictOper ['date'] = x.strftime("%x")
        with open('./ORDENES/operaciones.txt', 'a+') as f: ##En operaciones.txt tendremos 8 columnas 
            f.write("%s,%s,%s,%s,%d,%2.2f,%d,%s" % ((dictOper['date']),
                                                    (dictOper['varoOp']),
                                                    (dictOper['varcMer']),
                                                    (dictOper['varcSym']),
                                                    (dictOper['varoVo']),
                                                    (dictOper ['priceOrd']),
                                                    (dictOper['varoRe']),
                                                    (dictOper ['statusOrd'])) + '\n')
        print("GENERE OPERACION POR CONTRATO")
     
    def error(self,reqId, errorCode, errorString):
        print("Error:  ",reqId,"  ",errorCode,"  ",errorString)

    #Receives next valid order id. Will be invoked automatically upon successfull API client connection, or after
    #call to EClient::reqIds Important: the next valid order ID is only valid at the time it is received. 
    def nextValidId(self, orderId ):#Callback
        self.nextOrderId = orderId
        self.start()#Llama a la funcion de start ##Genera objeto contrato y order
        
    def contractDetails(self, reqId, contractDetails):  #Esto es una funcion de EWrapper function, es una clase de EWrapper
        #print("contractDetails:",reqId," ",contractDetails) #Esto lo que hace es imprimir la respuesta del callback que hace el EWrapper
        print("Este es el Mercado en la operacion: " + contractDetails.contract.primaryExchange)#Me sirve para conseguir el primaryExchange
        dictOper ['varcMer'] = contractDetails.contract.primaryExchange #varcMer / Mercado al cual pertenece el contrato en curso
        print("Asigne primaryExchange para los registros de: operaciones.txt")
        #self.disconnect()

    def orderStatus(self, orderId, status, filled, remaining, avgFillPrice, permId, parentId, lastFillPrice, clientId, whyHeld, mktCapPrice):
        print('orderStatus  Id:', orderId, 'status:', status, 'filled', filled, 'remaining', remaining, 'lastFillPrice', lastFillPrice)
        dictOper ['statusOrd'] = status
        dictOper ['priceOrd'] = lastFillPrice # al cual cerro posicion total o parcial 
        dictOper ['varoVo'] = filled #remaining #varoVo #Filled porque es el precio al cual cerro posicion
        dictOper ['varoRe'] = remaining #El volumen que queda pendiente de toda la orden
        print(dictOper ['statusOrd'])
        print(dictOper ['priceOrd'] )
        print(dictOper ['varoVo'])
        print(dictOper ['varoRe'])
        self.processOperations()

    def openOrder(self, orderId, contract:Contract, order:Order, orderState):#Revisar los parametros con la documentacion #EWrapper
        print('openOrder Id:', orderId, contract.symbol, contract.secType, '@', contract.exchange, contract.primaryExchange , ':', order.action, order.orderType, order.totalQuantity, orderState.status)
        print(contract.symbol)
        print(contract.exchange)
        print(contract.primaryExchange)##Por alguna razon esto lo deja vacio, no captura el primary.Exchange###Probado Varias Veces
        #print(varcMer)##Me imprime lo que tiene la variable varcMer
        dictOper ['varoOp'] = order.action #varoOp
        dictOper ['varoMax'] = order.lmtPrice #varoMax
        dictOper ['varcSym'] = contract.symbol #varcSym
        #dictOper ['varcMer'] = contract.primaryExchange #varcMer##No captura el valor de contract.primaryExchange
        #dictOper ['varcMer'] = contract.exchange ##En este caso coloca la variable "smart" ###Se esta usando otro formato de contrato
##### ALGUNA DE LAS DOS CLAVES ['varcMer'] DEBERIA SER ASIGNADA SINO ME DARA UN ERROR EN EL CODIGO. SI UTILIZO UNA FUNCIONA PERO ME DARA
##### UN RESULTADO NO DESEADO PERO SI ANULO LAS DOS EL CODIGO NO CORRE, TENDRA UN ERROR 

    def execDetails(self, reqId, contract, execution):
        print('executedDetails: ', reqId, contract.symbol, contract.secType, contract.currency, execution.execId, execution.orderId, execution.shares, execution.lastLiquidity, execution.price)
        print(execution.price)
        print(contract.exchange)
    
    
    def start(self):#Esta funcion genera un contrato  y objeto order
        
        contract = Contract()
        contract.symbol = varcSym #"AMZN"
        contract.secType = "STK"
        contract.exchange = "SMART" # Tengo inconveniente con esta
        contract.currency = "USD"
        contract.primaryExchange = varcMer #"NASDAQ"##Con el NASDAQ tipo string no funciona como debe

        print("Estoy en la funcion START " + contract.primaryExchange)    

        print("Estoy en la funcion START " + contract.exchange)

        order = Order()
        order.action = varoOp #"BUY" #"SELL"
        order.totalQuantity = varoVo #100
        order.orderType = "LMT"
        order.lmtPrice = varoMax #347.02
   
        self.reqContractDetails(0,contract)##Hago esto para asignar valor al varcMerc

        self.placeOrder(self.nextOrderId,contract,order)#places or modifies an order. #id,contract, order
        #self.reqContractDetails(0, contract)

    def stop(self):
        self.done = True
        self.disconnect()

def main():
    app = TestApp()
    app.nextorderId = 0
    app.connect("127.0.0.1", 7497, 0)
    #app.reqContractDetails(0, contract)#Esto es una funcion de EClient function, es una clase de EClient

    #Call stop() after 3 seconds to disconnect the program
    Timer(3, app.stop).start()#Al parecer se ejecuta el start() y el Timer como que espera 3 segundo para ejecutar el stop()
    app.run()#Comienza llamando a la funcion de error y asi sucesivamente

if __name__ == "__main__":
    main()
