from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum 

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)

    def processTickLine(self, line):
        print(line)
        with open('AAPLWithoutSmart1.out', 'a') as f:
            f.write(line + '\n')

    def error(self, reqId, errorCode, errorString):
        line = "Error: " + str(reqId) + "  " + str(errorCode) + " " + errorString
        #print("Error: ",reqId,"  ",errorCode," ",errorString)
        self.processTickLine(line)

    def tickPrice(self, reqId , tickType, price,attrib): #EWrapper Function
        line = "Tick Price. Ticket Id:" + str(reqId) + "tickType:" + TickTypeEnum.to_str(tickType) + "Price:" + str(price)
        self.processTickLine(line)
        #print("Tick Price. Ticket Id:", reqId, "tickType:", TickTypeEnum.to_str(tickType), "Price:", price, end='')
        
    def tickSize(self, reqId, tickType, size):
        line = "Tick Size.Ticker Id:" + str(reqId) + "tickType:" + TickTypeEnum.to_str(tickType) + "Size:" + str(size)
        self.processTickLine(line)
        #print("Tick Size.Ticker Id:", reqId, "tickType:", TickTypeEnum.to_str(tickType), "Size:", size)
    
def main():
    app = TestApp()
    #POR LOS DATOS QUE TENGO DEBERIA TRAERME PRECIO DE LAS ACCCIONES DEL INSTRUMENTO DECLARADO EN EL CONTRATO
    app.connect("127.0.0.1", 7497, 0)

    #Esta modificacion del contrato es para que me traiga datos de un solo exchange y no de varios, que "smart" me trae de varios
    contract = Contract()
    contract.symbol = "AAPL"
    contract.secType = "STK"
    contract.exchange = "ISLAND" #NASDAQ  #ISLAND
    contract.currency = "USD"
    
    #Contrato con atributos de contratos anteriores que funciona
    # contract = Contract()
    # contract.symbol = "AAPL"
    # contract.secType = "STK"
    # contract.exchange = "SMART"
    # contract.currency = "USD"
    # contract.primaryExchange = "NASDAQ" # Eliminada en la version corta de contrato

    #Esto son metodos de la clase EClient
    app.reqMarketDataType(4) # Este 4 es para delayed-frozen data
                
                #221= mark price (Precio de marca)
                #Identificador de la peticion = tickrId
                #(tickrId, contract, genericTickList(GenericTickTypes), snapshot, regulatorySnaphsot,mkdDataOptions)
    app.reqMktData(1,contract,"",False,False,[])
    app.run()

if __name__ == "__main__":
    main()
    