from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.common import BarData

import datetime

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        global myDict
        #myDict = {}
        #myDict ={'4':'0.0','6':'0.0','7':'0.0','9':'0.0','8':'0.0'}
        myDict ={'0':0,'1':0,'2':0,'3':0,'4':0} #Tener Diccionario con 0 por si un dato No viene.
    
    def processTickLine(self):
        print("GENERANDO FICHERO")
        x = datetime.datetime.now()
        print(x.strftime("%x"))
        myDict ['d'] = x.strftime("%x")
        with open('./historicos/idealpro/EUR.txt', 'a+') as f:
            f.write("%s,%2.2f,%2.2f,%2.2f,%2.2f,%i" % ((myDict['d']),
                                                    (myDict['0']),
                                                    (myDict['1']),
                                                    (myDict['2']),
                                                    (myDict['3']),
                                                    (myDict['4'])) + '\n')

    def error(self, reqId, errorCode, errorString):
        print("Error: ",reqId,"  ",errorCode," ",errorString)

    def historicalData(self,reqId,bar):
         myDict['1'] = bar.high
         myDict['2'] = bar.low
         myDict['3'] = bar.close
         myDict['4'] = bar.volume
        #print(bar.high)
        #print(bar.low)
        print("HistoricalData. ",reqId,
                "Date:",bar.date,
                "High:",bar.high,
                "Low:",bar.low,
                "Close:",bar.close,
                "Volume:",bar.volume,
                "Count", bar.barCount,
                "WAP:",bar.average)
                              
    
def main():
    app = TestApp()

    app.connect("127.0.0.1", 7497, 0)

    contract = Contract()
    contract.symbol = "EUR"
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