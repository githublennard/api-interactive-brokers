from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import *

import threading
import time

class IBapi(EWrapper, EClient):
	def __init__(self):
		EClient.__init__(self, self)

	def nextValidId(self, orderId: int):
		super().nextValidId(orderId)
		self.nextorderId = orderId
		print('The next valid order id is: ', self.nextorderId)

	def orderStatus(self, orderId, status, filled, remaining, avgFullPrice, permId, parentId, lastFillPrice, clientId, whyHeld, mktCapPrice):
		print('orderStatus - orderid:', orderId, 'status:', status, 'filled', filled, 'remaining', remaining, 'lastFillPrice', lastFillPrice)
	
	def openOrder(self, orderId, contract, order, orderState):
		print('openOrder id:', orderId, contract.symbol, contract.secType, '@', contract.exchange, ':', order.action, order.orderType, order.totalQuantity, orderState.status)

	def execDetails(self, reqId, contract, execution):
		print('Order Executed: ', reqId, contract.symbol, contract.secType, contract.currency, execution.execId, execution.orderId, execution.shares, execution.lastLiquidity)


def run_loop():
	app.run()

#Function to create FX Order contract
def FX_order(symbol):
	contract = Contract()
	contract.symbol = symbol[:3]
	contract.secType = 'CASH'
	contract.exchange = 'IDEALPRO'
	contract.currency = symbol[3:]
	return contract

app = IBapi()
app.connect('127.0.0.1', 7497, 123)

app.nextorderId = None

#Start the socket in a thread
api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()

#Check if the API is connected via orderid
while True:
	if isinstance(app.nextorderId, int):
		print('connected')
		break
	else:
		print('waiting for connection')
		time.sleep(1)

#Create order object
order = Order()
order.action = 'BUY'
order.totalQuantity = 100000
order.orderType = 'LMT'
order.lmtPrice = '1.10'

#Place order
app.placeOrder(app.nextorderId, FX_order('EURUSD'), order)
#app.nextorderId += 1

time.sleep(3)

#Cancel order 
print('cancelling order')
app.cancelOrder(app.nextorderId)

time.sleep(3)
app.disconnect()



# #Esta es una subclase hereda dos superclases
# class TestApp(EWrapper, EClient):
#     def __init__(self):
#         EClient.__init__(self,self) #Esto inicia conexion con los servidores de TWS IB

#     def error(self, reqId, errorCode, errorString):
#         print("Error: ",reqId,"  ",errorCode," ",errorString)

#     def contractDetails(self, reqId, contractDetails):  #Esto es una funcion de EWrapper function, es una clase de EWrapper
#         print("contractDetails:",reqId," ",contractDetails) #Esto lo que hace es imprimir la respuesta del callback que hace el EWrapper
#         print("End Contract Details")
#         self.disconnect()
        
# def main():
#     app = TestApp()

#     app.connect("127.0.0.1", 7497, 0)
#     time.sleep(2)

#     #Contrato Editado --->Como aparece en el Tutorial Video
#     contract = Contract()
#     contract.symbol = "AAPL"
#     contract.secType = "STK"
#     contract.exchange = "SMART"
#     contract.currency = "USD"
#     contract.primaryExchange = "NASDAQ"

#     #Contrato Original
#     # contract = Contract()
#     # contract.symbol = "AAPL"
#     # contract.secType = "STK"
#     # contract.currency = "USD"
#     # contract.primaryExchange = "NASDAQ"

#                             #(reqId, contract)
#     app.reqContractDetails(0, contract)#Esto es una funcion de EClient function, es una clase de EClient

#     app.run()
#     #time.sleep(5)
#     #app.disconnect()
    
# if __name__ == "__main__":
#     main()
    
