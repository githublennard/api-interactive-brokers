from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import *
from threading import Timer

import threading
import time
import datetime

import sys

global myOrderList
myOrderList = [] # Lista Vacia

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
# varoOp = "BUY"
# varoVoSo = 150
# varoMax = 360.45
# varcSym = "AAPL"
# varcMer = "ISLAND" #Se tiene que usar ISLAND en ves de "NASDAQ" 

# dictOper ['varoOp'] = varoOp ## Me dice si es BUY or SELL
# dictOper ['varoVoFi'] = varoVo #filled de orderStatus/ El volumen que se ejecuto
# dictOper ['varoMax'] = varoMax # Precio maximo que ofrezco
# dictOper ['varcSym'] = varcSym # Simbolo del activo
# dictOper ['varcMer'] = varcMer # Mercado al cual envio la orden
# dictOper ['varoRe'] = varoRe # remaining, lo que queda pendiente por ejecutar en el contrato

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)#Esto inicia conexion con los servidores de TWS IB
        global contador
        contador = 3
        #global dictOper
        #dictOper = {}
    
    def processOperations(self):
        global contador
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
        print("REGISTRO STATUS DE LA ORDEN EJECUTADA POR EL SISTEMA")
        
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

        print("DATOS DE LA ORDEN A EJCUTAR: " )    
        print(contract.symbol)
        print(contract.exchange)    

        order = Order()
        order.action = varoOp #"BUY" #"SELL"
        order.totalQuantity = varoVoSo #100
        order.orderType = "LMT"
        order.lmtPrice = varoMax #347.02
        print(varoVoSo)
   
        self.placeOrder(self.nextOrderId,contract,order)#places or modifies an order. #id,contract, order
        
    def stop(self):
        self.done = True
        self.disconnect()
        print("PASANDO POR STOP() Y REGRESA AL MAIN PARA REVISAR SI EXISTE OTRA ORDEN PARA EJECUTAR" + '\n')
        #newOrders()

def main():
    time.sleep(3)
    app = TestApp()
    app.nextorderId = 0
    app.connect("127.0.0.1", 7497, 0)
    time.sleep(3)
    print("PASANDO POR main() LUEGO POR app.run()")
    # # #Call stop() after 3 seconds to disconnect the program
                                 #Si desconecto el Timer me nunca termina el app.run()
                                 #La funcion start es del Timer no el start() de la clase TestApp
    Timer(6, app.stop).start()#Al parecer se ejecuta el start() y el Timer como que espera 6 segundo para ejecutar el stop()
    app.run() #Comienza llamando a la funcion de error y asi sucesivamente## Este da inicio a todo
              # Al parecer este llama openOrders() de primero y luego a start() que es una funcion que le pertenece a la Clase TestApp
              # Si ya existen ordenes abiertas esta va y las captura luego utiliza los datos nuevos para generar la orden nueva      
    print("EXISTEN MAS ORDENES ??? SINO EXISTE ORDENES A EJECUTAR LA PROXIMA FUNCION TERMINARA EL PROGRAMA")
    newOrders()##SI NO HAY MAS CONTRATOS REGRESA A LA SIGUIENTE LINEA Y SI HAY LA FUNCION LO MANDARA DIRECTO AL main()
    ##ESTA FUNCION LUEGO DE EJECUTAR REGRESA A LA SIGUIENTE LINEA Y SI HAY UN CONTRATO PENDIENTE LA FUNCION LO MANDARA DIRECTO AL main()
    
# if __name__ == "__main__":
#     main()

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

    #myList.remove(myList[0])
    #myList.remove(myList[0])
    
    if len(myOrderList) == 0:
        print("TERMINE TODAS LAS ORDENES")
        #app1.disconnect()##ESTE ESTARIA BIEN ESO CREO
        #exitContratos()
        #sys.exit(1)
        sys.exit()#ESTO FUNCIONA PERFECTAMENTE 
        #quit()
        #exit(0)    
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
    main()
    print("NO DEBERIA PASAR POR AQUI")


def readOrdenes():
    ###Es importante declarar aqui que las variables que se generan aqui son globales
    global varoOp #operacion contrato
    global varoVoSo #Numero (Volumen de activos o posicion Solicitados en la orden)
    global varoMax #Precio Maximo del stock
    global varcMer #Mercado
    global varcSym #Symbol
    #global myOrderList ##Ya estaba declarado al inicio del codigo

    with open('ordenes.txt','r') as file: #Este tiene coma en el texto 
        # reading each line	 
        for line in file:
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


readOrdenes()
main()
