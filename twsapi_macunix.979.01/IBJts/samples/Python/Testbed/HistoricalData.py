from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
#from ibapi.ticktype import TickTypeEnum

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)

    def error(self, reqId, errorCode, errorString):
        print("Error: ",reqId,"  ",errorCode," ",errorString)

    def historicalData(self,reqId,bar):
        print("HistoricalData. ",reqId,"Date:",bar.date,"High:",bar.high,"Low:",bar.low,"Close:",bar.close,"Volume:",bar.volume,"Count", bar.barCount,"WAP:",bar.average)
                                                                    #En esta concatenacion de argumentos, el orden es segun su descripcion en la documentacion                      
    # def tickPrice(self, reqId , tickType, price,attrib):
    #     print("Tick Price. Ticket Id:",reqId,"tickType:",TickTypeEnum.to_str(tickType),"Price:",price, end='')

    # def tickSize(self, reqId, tickType, size):
    #     print("Tick Size.Ticker Id:",reqId,"tickType:",TickTypeEnum.to_str(tickType),"Size:", size)

def main():
    app = TestApp()

    app.connect("127.0.0.1", 7497, 0)

    # contract = Contract()     #Con este tipo de contrato no funciona
    # contract.symbol = "AAPL"  
    # contract.secType = "STK"
    # contract.exchange = "SMART"
    # contract.currency = "USD"
    # #contract.primaryExchange = "NASDAQ"

    contract = Contract()
    contract.symbol = "EUR"
    contract.secType = "CASH"
    contract.exchange = "IDEALPRO"
    contract.currency = "USD"
    

    #Esto son metodos de la clase EClient
    #app.reqMarketDataType(4) # Este 4 es para delayed-frozen data

                #(tickrId, contract, genericTickList(GenericTickTypes), snapshot, regulatorySnaphsot,mkdDataOptions)
    #app.reqMktData(3,contract,"",False,False,[])
    
    app.reqHistoricalData(1,contract,"","1 D","1 min","BID",0,1,False,[])
         
    app.run()

if __name__ == "__main__":
    main()