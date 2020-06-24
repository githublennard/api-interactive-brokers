#Estos modulos contienen las clases
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import sys
import time
#Este codigo se conecta a TWS y a traves de la API me trae los detalles financieros del Instrumento

#Esta es una subclase hereda dos superclases
class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self) #Esto inicia conexion con los servidores de TWS IB

    def error(self, reqId, errorCode, errorString):
        print("Error: ",reqId,"  ",errorCode," ",errorString)

    def contractDetails(self, reqId, contractDetails):  #Esto es una funcion de EWrapper function, es una clase de EWrapper
        print("contractDetails:",reqId," ",contractDetails) #Esto lo que hace es imprimir la respuesta del callback que hace el EWrapper
        print(contractDetails.validExchanges)
        print(contractDetails.contract) #Me sirve pero me trae muchos detalles que no son necesarios
        print(contractDetails.contract.primaryExchange)#Me sirve para conseguir el primaryExchange
        print("End Contract Details")
        self.disconnect()
        
def main():
    app = TestApp()

    app.connect("127.0.0.1", 7497, 0)
    time.sleep(2)

    #Contrato Editado --->Como aparece en el Tutorial Video
    # contract = Contract()
    # contract.symbol = "AAPL"
    # contract.secType = "STK"
    # contract.exchange = "SMART"
    # contract.currency = "USD"
    # contract.primaryExchange = "NASDAQ"

    #Contrato Original ##Si uso este tipo de contratos no funciona ##Error:  0    200   No security definition has been found for the request 
    # contract = Contract()
    # contract.symbol = "AAPL"
    # contract.secType = "STK"
    # contract.currency = "USD"
    # contract.primaryExchange = "NASDAQ"##Da error 200 por este atributo

    contract = Contract()
    contract.symbol = "AMZN"
    contract.secType = "STK"
    contract.currency = "USD"
    #In the API side, NASDAQ is always defined as ISLAND in the exchange field
    contract.exchange = "ISLAND"

                            #(reqId, contract)
    app.reqContractDetails(0, contract)#Esto es una funcion de EClient function, es una clase de EClient

    app.run()
    #time.sleep(5)
    #app.disconnect()
    
if __name__ == "__main__":
    main()
    
