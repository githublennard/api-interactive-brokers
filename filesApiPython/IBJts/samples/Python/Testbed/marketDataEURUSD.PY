from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum 

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)

    def processTickLine(self, line):
        print(line)
        with open('eurosUSD.txt', 'a') as f:
            f.write(line + '\n')
        print("SALIENDO DE LINE")
    def error(self, reqId, errorCode, errorString):
        line = "Error: " + str(reqId) + "  " + str(errorCode) + " " + errorString
        #print("Error: ",reqId,"  ",errorCode," ",errorString)
        self.processTickLine(line)

    def tickPrice(self, reqId , tickType, price,attrib): #EWrapper Function
        line = "Tick Price. Ticket Id:" + str(reqId) + "tickType:" + TickTypeEnum.to_str(tickType) + "Price:" + str(price)
        print("POR AQUI PASO PRICE")
        print(TickTypeEnum.to_str(tickType))
        print(tickType)
        self.processTickLine(line)
        #print("Tick Price. Ticket Id:", reqId, "tickType:", TickTypeEnum.to_str(tickType), "Price:", price, end='')
        
    def tickSize(self, reqId, tickType, size):
        line = "Tick Size.Ticker Id:" + str(reqId) + "tickType:" + TickTypeEnum.to_str(tickType) + "Size:" + str(size)
        print("POR AQUI PASO SIZE")
        print(tickType)
        self.processTickLine(line)
        #print("Tick Size.Ticker Id:", reqId, "tickType:", TickTypeEnum.to_str(tickType), "Size:", size)
    
def main():
    app = TestApp()
    #POR LOS DATOS QUE TENGO DEBERIA TRAERME PRECIO DE LAS ACCCIONES DEL INSTRUMENTO DECLARADO EN EL CONTRATO
    app.connect("127.0.0.1", 7497, 0)

    contract = Contract()
    contract.symbol = "GBP"
    contract.secType = "CASH"
    contract.exchange = "IDEALPRO"
    contract.currency = "USD"

    # contract = Contract()
    # contract.symbol = "AAPL"
    # contract.secType = "STK"
    # contract.exchange = "SMART"
    # contract.currency = "USD"
    # contract.primaryExchange = "NASDAQ"

    #Esto son metodos de la clase EClient
    app.reqMarketDataType(4) # Este 4 es para delayed-frozen data
                
                #221= mark price (Precio de marca)
                #Identificador de la peticion = tickrId
                #(tickrId, contract, genericTickList(GenericTickTypes), snapshot, regulatorySnaphsot,mkdDataOptions)
    app.reqMktData(1,contract,"",False,False,[])
    app.run()

if __name__ == "__main__":
    main()
    