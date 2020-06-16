from ibapi.client import EClient
from ibapi.wrapper import EWrapper
import threading
import time
from ibapi.contract import Contract

class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
    def tickPrice(self, reqId, tickType, price, attrib):
        if tickType == 68 and reqId == 1:
            print('The current ask price is: ', price)


#def funcionTest(self,var1,var2):
def funcionTest():
    print("Aqui Test pero debo Regresar a Main")
    print(var1 + var2)

def run_loop():
    app.run()

app = IBapi()
app.connect('127.0.0.1', 7497, 123)

#Start the socket in a thread
api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()
global var1
global var2
va1 ='Mercado'
var2 = 'Instrumento'

time.sleep(1) #Sleep interval to allow time for connection to server

#Create contract object
apple_contract = Contract()
apple_contract.symbol = 'AAPL'
apple_contract.secType = 'STK'
apple_contract.exchange = 'SMART'
apple_contract.currency = 'USD'
#funcionTest()

app.reqMarketDataType(4)


#Request Market Data
app.reqMktData(1, apple_contract, '', False, False, [])
#app.funcionTest(var1,var2)

time.sleep(6)
app.disconnect()