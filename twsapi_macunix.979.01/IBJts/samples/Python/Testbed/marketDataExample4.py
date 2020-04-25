from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum #Esto se refiere al tipo tick que queremos, En este caso nos traera una lista
#Este codigo me trae el historico del precio de compra (BID) de un instrumento financiero

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)

    def error(self, reqId, errorCode, errorString):
        print("Error: ",reqId,"  ",errorCode," ",errorString)

    #def tickPrice(self, reqId , tickType, price,attrib): #EWrapper Function
    def tickPrice(self, reqId,BID, price, attrib):  # EWrapper Function
        f = open("./marketData/priceAppleStock.txt", "a") #Con este append 'a' agrega los datos uno tras otro
        print("Tick Price. Ticket Id:",reqId,"tickType:",TickTypeEnum.to_str(BID),"Price:",price, end='')
        #f.write(str("Tick Price. Ticket Id:",reqId,"tickType:",TickTypeEnum.to_str(tickType),"Price:",price, end=''))
        f.write(str(price))
        f.write(" ")
        
    #def tickSize(self, reqId, tickType, size):
    #    print("Tick Size.Ticker Id:", reqId, "tickType:", TickTypeEnum.to_str(tickType), "Size:", size)
    
def main():
    app = TestApp()
    #POR LOS DATOS QUE TENGO DEBERIA TRAERME PRECIO DE LAS ACCCIONES DEL INSTRUMENTO DECLARADO EN EL CONTRATO
    app.connect("127.0.0.1", 7497, 0)

    contract = Contract()
    contract.symbol = "AAPL"
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"
    contract.primaryExchange = "NASDAQ"

    #Esto son metodos de la clase EClient
    app.reqMarketDataType(4) # Este 4 es para delayed-frozen data
                
                #221= mark price (Precio de marca)
                #Identificador de la peticion = tickrId
                #(tickrId, contract, genericTickList(GenericTickTypes), snapshot, regulatorySnaphsot,mkdDataOptions)
    app.reqMktData(0,contract,"221",False,False,[])
    app.run()

if __name__ == "__main__":
    main()
    