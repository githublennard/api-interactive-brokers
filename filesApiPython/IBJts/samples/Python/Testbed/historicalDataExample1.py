from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)

    def error(self, reqId, errorCode, errorString):
        print("Error: ",reqId,"  ",errorCode," ",errorString)

    def historicalData(self,reqId,bar):
        print("HistoricalData. ",reqId,"Date:",bar.date,"High:",bar.high,"Low:",bar.low,"Close:",bar.close,"Volume:",bar.volume,"Count", bar.barCount,"WAP:",bar.average)
                                                                    #En esta concatenacion de argumentos, el orden es segun su descripcion en la documentacion                      

def main():
    app = TestApp()

    app.connect("127.0.0.1", 7497, 0)

    # contract = Contract()
    # contract.symbol = "IBDE30"
    # contract.secType = "CFD"
    # contract.currency = "EUR"
    # contract.exchange = "SMART"

    # contract = Contract()
    # contract.symbol = "DAX" #Historical Market Data Service error message:No market data permissions for DTB IND
    # contract.secType = "IND"
    # contract.currency = "EUR"
    # contract.exchange = "DTB"
    
    # contract = Contract()
    # contract.symbol = "IBKR"  #  No security definition has been found for the request
    # contract.secType = "STK"
    # contract.exchange = "IDEALPRO"
    # contract.currency = "USD"
    
    
    #Historical Market Data Service error message:No market data permissions for ISLAND STK
    # contract = Contract()
    # contract.symbol = "AAPL"
    # contract.secType = "STK"
    # contract.exchange = "SMART"
    # contract.currency = "USD"
    # # #contract.primaryExchange = "NASDAQ"

    #FUNCIONA
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