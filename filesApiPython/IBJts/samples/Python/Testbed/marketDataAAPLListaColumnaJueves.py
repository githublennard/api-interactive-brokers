from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum # Este modulo contiene en un vector con todos lo tickTypes disponibles

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        print("estoy en la clase")
        global line1
        line1 = 0  
        global line2
        line2 = 0
        global line3
        line3 = 0
        global line4
        line4 = 0
        global line5
        line5 = 0

            
    def processTickLine(self,line1,line2,line3,line4,line5):
        print("Estoy en el proceso de generar fichero")
        with open('./ficheros/AAPLColumna3.txt', 'a+') as f:
            f.write("%2.2f,%2.2f,%2.2f,%2.2f,%i" % (line1,line2,line3,line4,line5) + '\n')
            #f.write(line + '\n')
            #f.write("%2.2f,%2.2f,%2.2f,%2.2f,%2.2f,%i\n" % (line1,line2,line3,line4,line5))

    def error(self, reqId, errorCode, errorString):
        #line = "Error: " + str(reqId) + "  " + str(errorCode) + " " + errorString
        print("Error: ",reqId,"  ",errorCode," ",errorString)
        #self.processTickLine(line)

    def tickPrice(self, reqId ,tickType, price,attrib):
        if tickType == 68:
            line1 = float(price)
            print(TickTypeEnum.to_str(tickType), price)
            print("paso por el 68")
        # else:
        #     line1 = 0           
        if tickType == 72:
            line2 = float(price)
            print(TickTypeEnum.to_str(tickType), price)
            print("paso por el 72")      
        #else:
        #    line2 = 0
        if tickType == 73:
            line3 = float(price)
            print(TickTypeEnum.to_str(tickType), price)
            print("paso por el 73")
        #else:
        #    line3 = 0
        if tickType == 75:
            line4 = float(price)
            print(TickTypeEnum.to_str(tickType), price)
            print("paso por el 75")
            #break
        #else:
        #    line4 = 0

    def tickSize(self, reqId, tickType, size):
        if tickType == 74:
            line5 = int(size)
            print("Tick Size.Ticker Id:", reqId, "tickType:", TickTypeEnum.to_str(tickType), "Size:", size)
            self.processTickLine(line1,line2,line3,line4,line5)
            # if line1 != 0 and line2 != 0 and line3 != 0 and line4 != 0 and line5 != 0 : 
            #     self.processTickLine(line1,line2,line3,line4,line5)
            # else:
            #     print("paso por aqui")
            #     #break
                    
              
def main():
    print("estoy en el main")
    # global line1
    # line1 = 0  
    # global line2
    # line2 = 0
    # global line3
    # line3 = 0
    # global line4
    # line4 = 0
    # global line5
    # #line5 = 0
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
                #(tickrId, contract, genericTickList(GenericTickTypes), snapshot, regulatorySnaphsot,mkdDataOptions)
    app.reqMktData(0,contract,"",False,False,[])
    app.run()

if __name__ == "__main__":
    main()
    