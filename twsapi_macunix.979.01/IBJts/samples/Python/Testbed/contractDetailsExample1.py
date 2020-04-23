#Estos modulos contienen las clases
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract


#Esta es una subclase hereda dos superclases
class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self) #Esto inicia conexion con los servidores de TWS IB

    def error(self, reqId, errorCode, errorString):
        print("Error: ",reqId,"  ",errorCode," ",errorString)

    def contractDetails(self, reqId, contractDetails):  #Esto es una funcion de EWrapper function, es una clase de EWrapper
        f = open("contractMicrosoftDetails", "w+")
        print("contractDetails:",reqId," ",contractDetails) #Esto lo que hace es imprimir la respuesta del callback que hace el EWrapper
        f.write(str(contractDetails))
        f.close()

def main():
    app = TestApp()
                                    #El clientID debe cambiar para cada peticion
                       #(Ip,socketPort, clientID)
    app.connect("127.0.0.1", 7497, 1)
    print("serverVersion:%s connectionTime:%s" % (app.serverVersion(),
                                                  app.twsConnectionTime()))

    #Contrato Editado
    contract = Contract()
    #contract.symbol = "AAPL"
    contract.symbol = "MSFT"
    contract.secType = "STK" # Stock = Accion
    contract.exchange = "SMART"#Exchange: mercado donde se hacen las transacciones
    contract.currency = "USD"  #Este fue el campo que se añadio en el contrato
    contract.primaryExchange = "NASDAQ" #Exchange en este caso se califica como nativo para el tipo de contrato en caso de ambiguedad

    #Contrato Original
    # contract = Contract()
    # contract.symbol = "AAPL"
    # contract.secType = "STK"
    # contract.exchange = "USD"
    # contract.primaryExchange = "NASDAQ"

                            #(reqId, contract)
    app.reqContractDetails(0, contract)#Esto es una funcion de EClient function, es una clase de EClient

    app.run()

if __name__ == "__main__":
    main()
