from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum
import time
#CODIGO PARA VALIDAR FUNCIONAMIENTO DE LOS INTRUMENTOS FINANCIEROS TIPO STOCK STK (ACCIONES)
class TestApp(EWrapper, EClient):
    global contador
    contador = 5
    def __init__(self):
        EClient.__init__(self,self)

    def error(self, reqId, errorCode, errorString):
        print("Error: ",reqId,"  ",errorCode," ",errorString)

    def tickPrice(self, reqId , tickType, price,attrib):
        global contador
        print("Tick Price. Ticket Id:",reqId,"tickType:",TickTypeEnum.to_str(tickType),"Price:",price, end='')
        if contador == 5:
            self.disconnect()
        else: 
            contador += 1

    def tickSize(self, reqId, tickType, size):
        print("Tick Size.Ticker Id:",reqId,"tickType:",TickTypeEnum.to_str(tickType),"Size:", size)

def main():
    app = TestApp()

    app.connect("127.0.0.1", 7497, 0)
    
    contract = Contract()
    
    #contract.symbol = "SPY"
    #contract.symbol = "AGG"
    contract.symbol = "BLV"
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"
    #contract.currency = "EUR"
    contract.primaryExchange = "ARCA"

    time.sleep(3)
    #Esto son metodos de la clase EClient
    app.reqMarketDataType(4) # Este 4 es para delayed-frozen data

                #(tickrId, contract, genericTickList(GenericTickTypes), snapshot, regulatorySnaphsot,mkdDataOptions)
    app.reqMktData(0,contract,"",False,False,[])
    app.run()
    print("Elimino Conexion")
    app.disconnect()#Como que no funciona
if __name__ == "__main__":
    main()