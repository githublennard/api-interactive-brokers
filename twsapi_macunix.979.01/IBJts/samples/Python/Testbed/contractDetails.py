#Estos modulos contienen las clases
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract

#Este codigo se conecta a TWS y a traves de la API me trae los detalles financieros del Instrumento

#Esta es una subclase hereda dos superclases
class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self) #Esto inicia conexion con los servidores de TWS IB

    def error(self, reqId, errorCode, errorString):
        print("Error: ",reqId,"  ",errorCode," ",errorString)

    def contractDetails(self, reqId, contractDetails):  #Esto es una funcion de EWrapper function, es una clase de EWrapper
        print("contractDetails:",reqId," ",contractDetails) #Esto lo que hace es imprimir la respuesta del callback que hace el EWrapper

def main():
    app = TestApp()

    app.connect("127.0.0.1", 7497, 0)

    #Contrato Editado
    contract = Contract()
    contract.symbol = "AAPL"
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"
    contract.primaryExchange = "NASDAQ"

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
