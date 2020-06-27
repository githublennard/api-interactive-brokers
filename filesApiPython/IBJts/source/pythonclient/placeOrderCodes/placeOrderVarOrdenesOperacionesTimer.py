from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import *
from threading import Timer

import threading
import time
import datetime

global varoOp #operacion contrato
global varoVoSo #Numero (Volumen de activos o posicion Solicitados en la orden)
global varoMax #Precio Maximo del stock
global varcMer #Mercado
global varcSym #Symbol
global statusOrd 
global priceOrd
global dictOper
dictOper = {}

#Estas 5 variables debe ser leidas del archivo ordenes.txt
varoOp = "BUY"
varoVoSo = 150
varoMax = 361.20
varcSym = "AAPL"
varcMer = "ISLAND" #Se tiene que usar ISLAND en ves de "NASDAQ" 

# dictOper ['varoOp'] = varoOp ## Me dice si es BUY or SELL
# dictOper ['varoVoFi'] = varoVo #filled de orderStatus/ El volumen que se ejecuto
# dictOper ['varoMax'] = varoMax # Precio maximo que ofrezco
# dictOper ['varcSym'] = varcSym # Simbolo del activo
# dictOper ['varcMer'] = varcMer # Mercado al cual envio la orden
# dictOper ['varoRe'] = varoRe # remaining, lo que queda pendiente por ejecutar en el contrato

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
        #with open('./ORDENES/operaciones.txt', 'a+') as f: ##En operaciones.txt tendremos 8 columnas 
        with open('./operaciones.txt', 'a+') as f: ##En operaciones.txt tendremos 8 columnas 
            f.write("%s,%s,%s,%s,%d,%2.2f,%d,%s" % ((dictOper['date']),
                                                    (dictOper['varoOp']),
                                                    (dictOper['varcMer']),
                                                    (dictOper['varcSym']),
                                                    (dictOper['varoVoFi']),
                                                    (dictOper['priceOrd']),
                                                    (dictOper['varoRe']),
                                                    (dictOper['statusOrd'])) + '\n')
        print("GENERE REGISTRO DE OPERACION POR CONTRATO")

    #Receives next valid order id. Will be invoked automatically upon successfull API client connection, or after
    #call to EClient::reqIds Important: the next valid order ID is only valid at the time it is received. 
    def nextValidId(self, orderId): #Callback
        self.nextOrderId = orderId
        self.start() #Llama a la funcion de start ##Genera objeto contrato y order
        print("Estoy en nextValidId")

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
        dictOper ['varoOp'] = order.action #varoOp
        dictOper ['varoMax'] = order.lmtPrice #varoMax
        dictOper ['varcSym'] = contract.symbol #varcSym
        #dictOper ['varcMer'] = contract.primaryExchange #varcMer
        dictOper ['varcMer'] = contract.exchange ##Me muestra ordenes anteriores y la que corre actualmente 
                                                 ###Se esta usando otro formato de contrato

    def execDetails(self, reqId, contract, execution):
        print('executedDetails: ', reqId, contract.symbol, contract.secType, contract.currency, execution.execId, execution.orderId, execution.shares, execution.lastLiquidity, execution.price)
        print(execution.price)
        print(contract.exchange)
   
    def start(self):#Esta funcion genera un contrato  y objeto order
        
        contract = Contract()
        contract.symbol = varcSym #"AMZN"
        contract.secType = "STK"
        contract.currency = "USD"
        #In the API side, NASDAQ is always defined as ISLAND in the exchange field
        contract.exchange = varcMer #"ISLAND"

        print("Mercado donde se ejecuta la orden: " + contract.exchange)    

        order = Order()
        order.action = varoOp #"BUY" #"SELL"
        order.totalQuantity = varoVoSo #100
        order.orderType = "LMT"
        order.lmtPrice = varoMax #347.02
   
        self.placeOrder(self.nextOrderId,contract,order)#places or modifies an order. #id,contract, order
        
    def stop(self):
        self.done = True
        self.disconnect()

def main():
    app = TestApp()
    app.nextorderId = 0
    app.connect("127.0.0.1", 7497, 0)

    #app.start()
    ##app.stop()
    #app.run()
    #app.stop()

    # # #Call stop() after 3 seconds to disconnect the program
                                 #Si desconecto el Timer me nunca termina el app.run()
                                 #La funcion start es del Timer no el start() de la clase TestApp
    Timer(6, app.stop).start()#Al parecer se ejecuta el start() y el Timer como que espera 6 segundo para ejecutar el stop()
    app.run() #Comienza llamando a la funcion de error y asi sucesivamente## Este da inicio a todo


    #app.stop()##No funciona el app.run() no avanza a la siguiente linea
    #app.stop## No funciona

if __name__ == "__main__":
    main()
