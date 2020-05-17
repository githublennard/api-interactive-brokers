from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum 
import datetime

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        global myDict
        #myDict = {}
        #myDict ={'4':'0.0','6':'0.0','7':'0.0','9':'0.0','8':'0.0'}
        myDict ={'4':0,'6':0,'7':0,'9':0,'8':0} #Tener Diccionario con 0 por si un dato No viene.
            
    def processTickLine(self):
        print("GENERANDO FICHERO")
        x = datetime.datetime.now()
        print(x.strftime("%x"))
        myDict ['d'] = x.strftime("%x")
        with open('../historicos/idealpro/EUR.txt', 'a+') as f:
            f.write("%s,%2.2f,%2.2f,%2.2f,%2.2f,%i" % ((myDict['d']),
                                                    (myDict['4']),
                                                    (myDict['6']),
                                                    (myDict['7']),
                                                    (myDict['9']),
                                                    (myDict['8'])) + '\n')
            
    def error(self, reqId, errorCode, errorString):
        print("Error: ",reqId,"  ",errorCode," ",errorString)
        
    def tickPrice(self, reqId ,tickType, price,attrib):
        if tickType == 4:
            myDict['4'] = price
            print(TickTypeEnum.to_str(tickType),"Price:", price)
            if len(myDict) > 4:
                self.processTickLine()
                                         
        if tickType == 6:#Este tickType solo viene cuando cerro el mercado
            myDict['6'] = price
            print(TickTypeEnum.to_str(tickType),"Price:", price)
        
        if tickType == 7:#Este tickType solo viene cuando cerro el mercado
            myDict['7'] = price
            print(TickTypeEnum.to_str(tickType),"Price:", price)
        
        if tickType == 9:#Este tickType solo viene una vez
            myDict['9'] = price
            print(TickTypeEnum.to_str(tickType),"Price:", price)
            if len(myDict) > 4:
                self.processTickLine()
        
    def tickSize(self, reqId, tickType, size):
        if tickType == 8:
            myDict['8'] = size
            print(TickTypeEnum.to_str(tickType), "Size:", size)
            if len(myDict) > 4:
               self.processTickLine() 
              
def main():
    
    app = TestApp()
    app.connect("127.0.0.1", 7497, 0)
    print("serverVersion:%s connectionTime:%s" % (app.serverVersion(),
                                                  app.twsConnectionTime()))
    
    contract = Contract()
    contract.symbol = "GBP"
    contract.secType = "CASH"
    contract.exchange = "IDEALPRO"
    contract.currency = "USD"
    #contract.primaryExchange = "ISLAND"   #"NASDAQ",SE PUEDE USAR ISLAND INSTEAD NASDAQ

        #Esto son metodos de la clase EClient
    app.reqMarketDataType(4) # Este 4 es para delayed-frozen data
                
                #(tickrId, contract, genericTickList(GenericTickTypes), snapshot, regulatorySnaphsot,mkdDataOptions)
    app.reqMktData(0,contract,"",False,False,[])
    app.run()

if __name__ == "__main__":
    main()
    