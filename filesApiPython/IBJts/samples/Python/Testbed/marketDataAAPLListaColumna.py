from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum # Este modulo contiene en un vector todos lo tickTypes disponibles

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        global line1  
        global line2
        global line3
        global line4
        global line5
        global values
    
    def processTickLine(self,line1,line2,line3,line4,line5 ):
        print(line1+line2)
        with open('AAPLColumna.out', 'a+') as f:
            f.write("%2.2f,%2.2f,%2.2f,%2.2f,%2.2f" % (line1,line2,line3,line4,line5) + '\n')
            #f.write(line + '\n')
            #f.write("%2.2f,%2.2f,%2.2f,%2.2f,%2.2f,%i\n" % (line1,line2,line3,line4,line5))

    def error(self, reqId, errorCode, errorString):
        #line = "Error: " + str(reqId) + "  " + str(errorCode) + " " + errorString
        print("Error: ",reqId,"  ",errorCode," ",errorString)
        #self.processTickLine(line)

    def tickPrice(self, reqId ,tickType, price,attrib):
        global line1
        global line2
        global line3
        global line4
        global line5
        global values
        if tickType == 68:
            line1 = int(price)
            #line1 = TickTypeEnum.to_str(tickType) + str(price)
            #self.processTickLine(line)
            print(TickTypeEnum.to_str(tickType), price)
        if tickType == 72:
            line2 = int(price)
            #line2 = TickTypeEnum.to_str(tickType) + str(price)
            #self.processTickLine(line)
            print(TickTypeEnum.to_str(tickType), price)
        if tickType == 73:
            line3 = int(price)
            #line3 = TickTypeEnum.to_str(tickType) + str(price)
            #self.processTickLine(line)
            print(TickTypeEnum.to_str(tickType), price)
        if tickType == 75:
            line4 = int(price)
            #line4 = TickTypeEnum.to_str(tickType) + str(price)
            #self.processTickLine(line)
            print(TickTypeEnum.to_str(tickType), price)
        else:
            line4 = 0

    def tickSize(self, reqId, tickType, size):
        if tickType == 74:
            line5 = int(size)
            #line5 = TickTypeEnum.to_str(tickType) + str(size)
            #self.processTickLine(line)
            print("Tick Size.Ticker Id:", reqId, "tickType:", TickTypeEnum.to_str(tickType), "Size:", size)
            if line1 != None and line2 != None and line3 != None and line4 != None and line5 != None : 
                self.processTickLine(line1,line2,line3,line4,line5)
            else:
                print("paso por aqui")
                    
        
    # def filled(self,line1,line2,line3,line4,line5):
    #     global values
    #     values = [line1,line2,line3,line4,line5]
    #     for i in values:
    #         if i == 0 :
    #             main()
    #         else:
    #             self.processTickLine(values)
            
            

                 
  
def main():
    app = TestApp()
    #POR LOS DATOS QUE TENGO DEBERIA TRAERME PRECIO DE LAS ACCCIONES DEL INSTRUMENTO DECLARADO EN EL CONTRATO
    app.connect("127.0.0.1", 7497, 0)

    contract = Contract()
    contract.symbol = "AAPL"
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"
    contract.primaryExchange = "ISLAND"   #"NASDAQ",SE PUEDE USAR ISLAND INSTEAD NASDAQ

    # contract = Contract()
    # contract.symbol = "AAPL"
    # contract.secType = "STK"
    # contract.exchange = "ISLAND" #Este contrato no corre si estoy en la sesion de tfm2020le, pero si corre en la sesion "demo TWS"
    # contract.currency = "USD"


    #Esto son metodos de la clase EClient
    app.reqMarketDataType(4) # Este 4 es para delayed-frozen data
                
                                    #221= mark price (Precio de marca), esto es referente al genericTickList(GenericTickTypes)
                #Identificador de la peticion = tickrId
                #(tickrId, contract, genericTickList(GenericTickTypes), snapshot, regulatorySnaphsot,mkdDataOptions)
    app.reqMktData(0,contract,"",False,False,[])
    app.run()

if __name__ == "__main__":
    main()
    