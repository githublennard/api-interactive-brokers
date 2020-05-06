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
        f = open("./historicalData/historicalDataEUR123.txt", "a")             ##En esta concatenacion de argumentos de bar, el orden es segun su descripcion en la documentacion
        info = print("HistoricalData. ",reqId,"Date:",bar.date,"High:",bar.high,"Low:",bar.low,"Close:",bar.close,"Volume:",bar.volume,"Count", bar.barCount,"WAP:",bar.average)
        f.write(str(bar.high)) #Donde bar.high es el precio mas alto del instrumento
        f.write(" ")                                                                                  

def main():
    app = TestApp()

    app.connect("127.0.0.1", 7497, 0)

    
    #FUNCIONA
    contract = Contract()
    contract.symbol = "EUR"
    contract.secType = "CASH"
    contract.exchange = "IDEALPRO"
    contract.currency = "USD"
    

    app.reqHistoricalData(1,contract,"","1 D","1 min","MIDPOINT",0,1,False,[])
         
    app.run()

if __name__ == "__main__":
    main()