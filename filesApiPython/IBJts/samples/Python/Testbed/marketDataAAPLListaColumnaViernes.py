from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum # Este modulo contiene en un vector con todos lo tickTypes disponibles

import datetime

#x = datetime.datetime.now()
#print(x.strftime("%x"))

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        print("estoy en la clase")
        global myDict
        myDict = {}
        #myDict ={'68':'0','72':'0','73':'0','75':'0','74':'0'}
            
    def processTickLine(self):
        print("Estoy en el proceso de generar fichero")
        x = datetime.datetime.now()
        print(x.strftime("%x"))
        myDict ['d'] = x.strftime("%x")
        with open('./ficheros/AAPLrqMarketData.txt', 'a+') as f:
            f.write("%s,%2.2f,%2.2f,%2.2f,%2.2f,%i" % ((myDict['d']),
                                                    (myDict['68']),
                                                    (myDict['72']),
                                                    (myDict['73']),
                                                    (myDict['75']),
                                                    (myDict['74'])) + '\n')
            #f.write( str(myDict['68'])+ str(myDict['74']) +'\n' )#funciona
            #f.write( str(myDict))#funciona
            #f.write("%2.2f,%2.2f,%2.2f,%2.2f,%i" % (line1,line2,line3,line4,line5) + '\n')
            #f.write(line + '\n')
            #f.write("%2.2f,%2.2f,%2.2f,%2.2f,%2.2f,%i\n" % (line1,line2,line3,line4,line5))

    def error(self, reqId, errorCode, errorString):
        #line = "Error: " + str(reqId) + "  " + str(errorCode) + " " + errorString
        print("Error: ",reqId,"  ",errorCode," ",errorString)
        #self.processTickLine(line)

    def tickPrice(self, reqId ,tickType, price,attrib):
        if tickType == 68:
            myDict['68'] = price
            print(TickTypeEnum.to_str(tickType), price)
            if len(myDict) > 4:
               self.processTickLine()
            #myDict['68'] = float(price) 
            #dict['School'] = "DPS School"; # Add new entry
            print(TickTypeEnum.to_str(tickType), price)
            #print(app.reqCurrentTime())
            #print(app.twsConnectionTime())
                             
        if tickType == 72:#Este tickType solo viene cuando cerro el mercado
            myDict['72'] = price
            print(TickTypeEnum.to_str(tickType), price)
        
        if tickType == 73:#Este tickType solo viene cuando cerro el mercado
            myDict['73'] = price
            print(TickTypeEnum.to_str(tickType), price)
        
        if tickType == 75:#Este tickType solo viene una vez
            myDict['75'] = price
            print(TickTypeEnum.to_str(tickType), price)
            #print("paso por el 75")
            if len(myDict) > 4:
               self.processTickLine()
        
    def tickSize(self, reqId, tickType, size):
        if tickType == 74:
            myDict['74'] = size
            print("Tick Size.Ticker Id:", reqId, "tickType:", TickTypeEnum.to_str(tickType), "Size:", size)
            if len(myDict) > 4:
               self.processTickLine() 
              
def main():
    
    app = TestApp()
    app.connect("127.0.0.1", 7497, 0)
    print("serverVersion:%s connectionTime:%s" % (app.serverVersion(),
                                                  app.twsConnectionTime()))
    
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
                
                #(tickrId, contract, genericTickList(GenericTickTypes), snapshot, regulatorySnaphsot,mkdDataOptions)
    app.reqMktData(0,contract,"",False,False,[])
    app.run()

if __name__ == "__main__":
    main()
    