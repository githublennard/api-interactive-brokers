from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum 
import datetime
import time

global myList
global app
global var1
global var2

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        global myDict
        #myDict = {}
        #myDict ={'68':'0.0','72':'0.0','73':'0.0','75':'0.0','74':'0.0'}
        myDict ={'68':0,'72':0,'73':0,'75':0,'74':0} #Tener Diccionario con 0 por si un dato No viene.
        global contador
        contador = 3

    def processTickLine(self):
        global contador
        #global var1
        #global var2
        print("GENERANDO FICHERO")
        x = datetime.datetime.now()
        print(x.strftime("%x"))
        myDict ['d'] = x.strftime("%x")
        #with open('./DATOS/NASDAQ/AAPL.txt', 'a+') as f:
        #with open('./DATOS/var1/var2.txt', 'a+') as f:
        with open(('./DATOS/%s/%s.txt' % (var1,var2)), 'a+') as f:
            f.write("%s,%2.2f,%2.2f,%2.2f,%2.2f,%i" % ((myDict['d']),
                                                    (myDict['68']),
                                                    (myDict['72']),
                                                    (myDict['73']),
                                                    (myDict['75']),
                                                    (myDict['74'])) + '\n')
        print("Pasando Por Contador")
        contador -= 1
        print(contador)
        if contador == 0:
            print("Termine escribir data Contrato")
            self.otroContrato()
            #self.disconnect()
        else:
            print("Faltan lineas para terminar el contrato")   

    def error(self, reqId, errorCode, errorString):
        print("Error: ",reqId,"  ",errorCode," ",errorString)
        
    def tickPrice(self, reqId ,tickType, price,attrib):
        if tickType == 68:
            myDict['68'] = price
            print(TickTypeEnum.to_str(tickType),"Price:", price)
            if len(myDict) > 4:
                self.processTickLine()
                                         
        if tickType == 72:#Este tickType solo viene cuando cerro el mercado
            myDict['72'] = price
            print(TickTypeEnum.to_str(tickType),"Price:", price)
        
        if tickType == 73:#Este tickType solo viene cuando cerro el mercado
            myDict['73'] = price
            print(TickTypeEnum.to_str(tickType),"Price:", price)
        
        if tickType == 75:#Este tickType solo viene una vez
            myDict['75'] = price
            print(TickTypeEnum.to_str(tickType),"Price:", price)
            if len(myDict) > 4:
                self.processTickLine()
        
    def tickSize(self, reqId, tickType, size):
        if tickType == 74:
            myDict['74'] = size
            print(TickTypeEnum.to_str(tickType), "Size:", size)
            if len(myDict) > 4:
               self.processTickLine() 
    
    def otroContrato(self):
        #self.cancelMktData(0)
        self.disconnect()# Cancelo Conexion para iniciar nueva conexion con otro objeto
        time.sleep(3)
        print("Tratando de Implementar otro contrato")
        while len(myList) > 0:
            #del app # Elimino objeto de la clase # No funciona lo toma como una variable local
            # myList.remove(myList[0])
            # myList.remove(myList[0])
            print(myList)
            #self.main1()
            main1() #Aqui llamo a una funcion fuera de la clase y funciona
        else:
            print("Termine el While de  otro contrato")
            self.disconnect()
            return #agregue este
            #self.main1()
        #self.disconnect()
        
              
def main():
    
    global app
    app = TestApp()
    app.connect("127.0.0.1", 7497, 0)
    print("serverVersion:%s connectionTime:%s" % (app.serverVersion(),app.twsConnectionTime()))
    global var1
    global var2
    global myList
    myList = [] # Lista
    
    # var1 = 'NASDAQ' #Con estas variables pude generar los contratos 
    # var2 = 'AAPL'   #Faltaria ingresar que los capture desde la lectura y regese al contrato
    with open('paraLeer.txt','r') as file: 
        # reading each line	 
        for line in file: 
            # reading each word		 
            #for word in line.split(",",1): #Si hago esplit de 1 me devuelve una lista de 2 elementos
            for word in line.split(): #Con el separador de espacio por defecto me devuelve lo que necesito
                # displaying the words		 
                print(word)
                myList.append(word)
                
            print("Termine leer todas las lineas")
        print("Asigno Posicion primer contrato")	
        var1 = myList[0]
        var2 = myList[1]
        print(myList)
        print("Termine el bucle de for y lectura del archivo.txt / Tengo un array de contratos")

    time.sleep(3)   

    contract = Contract()
    contract.symbol = var2                #variable 2
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"
    contract.primaryExchange = var1     #variable 1 

        #Esto son metodos de la clase EClient
    app.reqMarketDataType(4) # Este 4 es para delayed-frozen data
                
                #(tickrId, contract, genericTickList(GenericTickTypes), snapshot, regulatorySnaphsot,mkdDataOptions)
    app.reqMktData(0,contract,"",False,False,[])
    app.run()


def main1():
    global app1
    global var1
    global var2 
    global myList
    print("Se supone que elimine conexion del objeto anterior de la clase TestApp que es global")
    myList.remove(myList[0])
    myList.remove(myList[0])
    
    if len(myList) == 0:
        print("Termine todos los contratos")
        #app.disconnect()
        return
    var1 = myList[0]
    var2 = myList[1]
    
    print(myList)
    print("La lista que se muestra en pantalla ya tiene menos dos elementos")
    # if len(myList) == 0:
    #     print("Termine")
    #     app.disconnect()
    #     return 
    
    print("Se supone que voy a crear un nuevo contrato, por eso vuelvo a llamar a la clase,Inicio nueva conexion")
    app1 = TestApp()
    app1.connect("127.0.0.1", 7497, 0)
    time.sleep(3)
    contract = Contract()
    contract.symbol = var2                #variable 2
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"
    contract.primaryExchange = var1 

    app1.reqMarketDataType(4)
    app1.reqMktData(0,contract,"",False,False,[])
    app1.run()
    print("Termino el objeto de la clase")# Pasa por aqui luego de que termino todos los contratos, No deberia

    # else:
    #     print("Faltan Contratos para terminar")   
    # #############################################################3
    # while len(myList) > 0:
    #     myList.remove(myList[0])
    #     myList.remove(myList[0])
    #     var1 = myList[0]
    #     var2 = myList[1]
    #     print(myList)
    #     contract = Contract()
    #     contract.symbol = var2                #variable 2
    #     contract.secType = "STK"
    #     contract.exchange = "SMART"
    #     contract.currency = "USD"
    #     contract.primaryExchange = var1     #variable 1 
    #     del app
    #     print("Se supone que cree un nuevo contrato, por eso vuelvo a llamar")
    #     app = TestApp()
    #     app.connect("127.0.0.1", 7497, 0)
    #     app.reqMarketDataType(4)
    #     app.reqMktData(0,contract,"",False,False,[])
    #     print("Nuevo contrato en ejecucion")
    
    # else:
    #     print("Termine el While")
    #######################################################################
    # contract = Contract()
    # contract.symbol = var2                #variable 2
    # contract.secType = "STK"
    # contract.exchange = "SMART"
    # contract.currency = "USD"
    # contract.primaryExchange = var1     #variable 1 
    
    # print("Se supone que cree un nuevo contrato, por eso vuelvo a llamar")
    # app.reqMktData(0,contract,"",False,False,[])
    # print("Nuevo contrato en ejecucion")

    
main()
#main1()

# if __name__ == "__main__":
#      main()
    