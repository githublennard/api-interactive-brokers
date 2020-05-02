from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum # Este modulo contiene en un vector todos lo tickTypes disponibles

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)

    def processTickLine(self, line):
        print(line)
        with open('ABBVLISTA.out', 'a') as f:
            f.write(line + '\n')

    def error(self, reqId, errorCode, errorString):
        line = "Error: " + str(reqId) + "  " + str(errorCode) + " " + errorString
        #print("Error: ",reqId,"  ",errorCode," ",errorString)
        self.processTickLine(line)

    def tickPrice(self, reqId ,tickType, price,attrib):
        if tickType == 68:
            line = TickTypeEnum.to_str(tickType) + str(price)
            self.processTickLine(line)  
            #print(TickTypeEnum.to_str(tickType), price)
        if tickType == 72:
            line = TickTypeEnum.to_str(tickType) + str(price)
            self.processTickLine(line)  
            #print(TickTypeEnum.to_str(tickType), price)
        if tickType == 73:
            line = TickTypeEnum.to_str(tickType) + str(price)
            self.processTickLine(line)  
            #print(TickTypeEnum.to_str(tickType), price)
        if tickType == 75:
            line = TickTypeEnum.to_str(tickType) + str(price)
            self.processTickLine(line)  
            #print(TickTypeEnum.to_str(tickType), price)
        
    def tickSize(self, reqId, tickType, size):
        if tickType == 74:
            line = TickTypeEnum.to_str(tickType) + str(size)
            self.processTickLine(line)  
            
  
def main():
    app = TestApp()
    #POR LOS DATOS QUE TENGO DEBERIA TRAERME PRECIO DE LAS ACCCIONES DEL INSTRUMENTO DECLARADO EN EL CONTRATO
    app.connect("127.0.0.1", 7497, 0)

    contract = Contract()
    contract.symbol = "ABBV"
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"
    contract.primaryExchange = "ISLAND"   #"NASDAQ",SE PUEDE USAR ISLAND INSTEAD NASDAQ

    #Esto son metodos de la clase EClient
    app.reqMarketDataType(4) # Este 4 es para delayed-frozen data
                
                                    #221= mark price (Precio de marca), esto es referente al genericTickList(GenericTickTypes)
                #Identificador de la peticion = tickrId
                #(tickrId, contract, genericTickList(GenericTickTypes), snapshot, regulatorySnaphsot,mkdDataOptions)
    app.reqMktData(1,contract,"",False,False,[])
    app.run()

if __name__ == "__main__":
    main()
    