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
        print("HistoricalData. ",reqId,
                "Date:",bar.date,
                "High:",bar.high,
                "Low:",bar.low,
                "Close:",bar.close,
                "Volume:",bar.volume,
                "Count", bar.barCount,
                "WAP:",bar.average)
                                                                    #En esta concatenacion de argumentos, el orden es segun su descripcion en la documentacion                      
    
def main():
    app = TestApp()

    app.connect("127.0.0.1", 7497, 0)

    contract = Contract()
    contract.symbol = "IBEX35"  # No market data permissions for NYSE STK -->>  For Live TWS
    contract.secType = "IND"
    contract.exchange = "MEFFRV"
    contract.currency = "EUR"

    #contract = Contract()
    #contract.symbol = "MGM"  # No market data permissions for NYSE STK -->>  For Live TWS
    #contract.secType = "STK"
    #contract.exchange = "SMART"
    #contract.currency = "USD"

    #contract = Contract()
    #contract.symbol = "UAVS" #No market data permissions for AMEX STK-->> For Live TWS
    #contract.secType = "STK"
    #contract.exchange = "SMART"  # Este contrato no corre si estoy en la sesion de tfm2020le, pero si corre en la sesion "demo TWS"
    #contract.currency = "USD"

    #contract = Contract()
    #contract.symbol = "IBKR"
    #contract.secType = "STK"
    #contract.exchange = "SMART"  # Este contrato no corre si estoy en la sesion de tfm2020le, pero si corre en la sesion "demo TWS"
    #contract.currency = "USD"

    #contract = Contract()
    #contract.symbol = "GBP"
    #contract.secType = "CASH"
    #contract.exchange = "IDEALPRO" #Este contrato no corre si estoy en la sesion de tfm2020le, pero si corre en la sesion "demo TWS"
    #contract.currency = "USD"

    #contract = Contract()     #Con este tipo de contrato no funciona
    #contract.symbol = "AAPL"  #No market data permissions for ISLAND STK en version DEMO
    #contract.secType = "STK"  #No market data permissions for ISLAND STK en version tfm2020le
    #contract.exchange = "SMART"
    #contract.currency = "USD"
    #contract.primaryExchange = "NASDAQ"

    # contract = Contract()
    # contract.symbol = "EUR"
    # contract.secType = "CASH"
    # contract.exchange = "IDEALPRO" #Este contrato no corre si estoy en la sesion de tfm2020le, pero si corre en la sesion "demo TWS"
    # contract.currency = "USD"
    
#idRequest,contract,EndDay(Se puede especificar el dia que queremos data)",Duration,Bar(size),typeData(BID,ASK,etc),0(trading hours),1(format data), Bool,Attribute
    app.reqHistoricalData(1,contract,"","1 D","1 min","MIDPOINT",0,1,False,[])
         
    app.run()

if __name__ == "__main__":
    main()