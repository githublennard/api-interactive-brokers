from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import *
from threading import Timer

import threading
import time

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)#Esto inicia conexion con los servidores de TWS IB

    def error(self,reqId, errorCode, errorString):
        print("Error:  ",reqId,"  ",errorCode,"  ",errorString)

    #Receives next valid order id. Will be invoked automatically upon successfull API client connection, or after
    #call to EClient::reqIds Important: the next valid order ID is only valid at the time it is received. 
    def nextValidId(self, orderId ):#Callback
        self.nextOrderId = orderId
        self.start()#Llama a la funcion de start

    def orderStatus(self, orderId, status, filled, remaining, avgFillPrice, permId, parentId, lastFillPrice, clientId, whyHeld, mktCapPrice):
        print('orderStatus.Id:', orderId, 'status:', status, 'filled', filled, 'remaining', remaining, 'lastFillPrice', lastFillPrice)
    
    def openOrder(self, orderId, contract:Contract, order:Order, orderState):#Revisar los parametros con la documentacion #EWrapper
        print('openOrder id:', orderId, contract.symbol, contract.secType, '@', contract.exchange, ':', order.action, order.orderType, order.totalQuantity, orderState.status)

    def execDetails(self, reqId, contract, execution):
        print('executedDetails: ', reqId, contract.symbol, contract.secType, contract.currency, execution.execId, execution.orderId, execution.shares, execution.lastLiquidity)

    def start(self):#Esta funcion genera un contrato  y objeto order
        
        contract = Contract()
        contract.symbol = "AAPL"
        contract.secType = "STK"
        contract.exchange = "SMART"
        contract.currency = "USD"
        contract.primaryExchange = "NASDAQ"

        order = Order()
        order.action = "BUY" #"SELL"
        order.totalQuantity = 11
        order.orderType = "LMT"
        order.lmtPrice = 346.67

        self.placeOrder(self.nextOrderId,contract,order)#places or modifies an order. #id,contract, order

    def stop(self):
        self.done = True
        self.disconnect()

def main():
    app = TestApp()
    app.nextorderId = 0
    app.connect("127.0.0.1", 7497, 0)

    #Call stop() after 3 seconds to disconnect the program
    Timer(3, app.stop).start()#Al parecer se ejecuta el start() y el Timer como que espera 3 segundo para ejecutar el stop()
    app.run()#Comienza llamando a la funcion de error y asi sucesivamente

if __name__ == "__main__":
    main()
