from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.common import BarData

import datetime

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        global myDict
            
    def processTickLine(self, line):
        print("GENERANDO LINEA")
        with open('../historicos/idealpro/GBP.txt', 'a') as f:
            f.write(line + '\n')
        
    def error(self, reqId, errorCode, errorString):
        print("Error: ",reqId,"  ",errorCode," ",errorString)

    def historicalData(self,reqId,bar):
        line = str(bar.date) +","+ str(bar.high) + "," +str(bar.low)+","+str(bar.close)+","+str(bar.volume)
        print("HistoricalData. ",reqId,
                "Date:",bar.date,
                "High:",bar.high,
                "Low:",bar.low,
                "Close:",bar.close,
                "Volume:",bar.volume,
                "Count", bar.barCount,
                "WAP:",bar.average)
        self.processTickLine(line)
                              
    
def main():
    app = TestApp()

    app.connect("127.0.0.1", 7497, 0)

    contract = Contract()
    contract.symbol = "GBP"
    contract.secType = "CASH"
    contract.exchange = "IDEALPRO" #Este contrato no corre si estoy en la sesion de tfm2020le, pero si corre en la sesion "demo TWS"
    contract.currency = "USD"
    

    #yyyymmdd HH:mm:ss ttt
#idRequest,contract,EndDay(Se puede especificar el dia que queremos data)",Duration,Bar(size),typeData(BID,ASK,etc),0(trading hours),1(format data), Bool,Attribute
    #app.reqHistoricalData(1,contract,"20200801 23:59:59 GMT","1 D","1 min","MIDPOINT",0,1,False,[])
    app.reqHistoricalData(1,contract,"","1 D","1 min","MIDPOINT",0,1,False,[])     
    app.run()

if __name__ == "__main__":
    main()