from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum #Esto se refiere al tipo tick que queremos, En este caso nos traera una lista

class TestApp(EWrapper, EClient):
    global f
    def __init__(self):
        EClient.__init__(self,self)

    def error(self, reqId, errorCode, errorString):
        print("Error: ",reqId,"  ",errorCode," ",errorString)

    def tickPrice(self, reqId , tickType, price,attrib): #EWrapper Function
        #f = open("priceAppleStock", "w+")
        f = open("priceAmazonStock", "a") #Con este append 'a' si funciona me agrega los datos uno tras otro
        print("Tick Price. Ticket Id:",reqId,"tickType:",TickTypeEnum.to_str(tickType),"Price:",price, end='')
        #f.write(str("Tick Price. Ticket Id:",reqId,"tickType:",TickTypeEnum.to_str(tickType),"Price:",price, end=''))
        f.write(str(price))
        f.write(" ")
        #f.write(str(price + " "))
        #f.write(str(price," ")) # tampoco funcion con ""
        #f.write(str(price, end=''))
        #f.close()
    def tickSize(self, reqId, tickType, size):
        print("Tick Size.Ticker Id:", reqId, "tickType:", TickTypeEnum.to_str(tickType), "Size:", size)
    #def tickSize(self, reqId, tickType, size):           #EWrapper Function
        #print("Tick Size.Ticker Id:",reqId,"tickType:",TickTypeEnum.to_str(tickType),"Size:", size)

def main():
    app = TestApp()
    #POR LOS DATOS QUE TENGO DEBERIA TRAERME PRECIO DE LAS ACCCIONES DEL INSTRUMENTO DECLARADO EN EL CONTRATO
    app.connect("127.0.0.1", 7497, 0)

    contract = Contract()
    contract.symbol = "AMZN"
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"
    contract.primaryExchange = "NASDAQ"

    #Esto son metodos de la clase EClient
    app.reqMarketDataType(4) # Este 4 es para delayed-frozen data
                
                #Identificador de la peticion = tickrId
                #(tickrId, contract, genericTickList(GenericTickTypes), snapshot, regulatorySnaphsot,mkdDataOptions)
    app.reqMktData(0,contract,"",False,False,[])
    app.run()

if __name__ == "__main__":
    #global f
    #f = open("priceAppleStock", "a")
    main()
    #f.close()