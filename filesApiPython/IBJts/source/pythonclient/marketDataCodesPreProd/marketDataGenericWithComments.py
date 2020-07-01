from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum 
import datetime
import time
import sys

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
        print(var1)
        dirName = "./DATOS/var1/"
        # Create target Directory if don't exist
        if not os.path.exists(dirName):
            os.mkdir(dirName)
            print("Directory " , dirName ,  " Created ")
        else:
            print("Directory " , dirName ,  " already exists")
        
        print("GENERANDO FICHERO")
        x = datetime.datetime.now()
        print(x.strftime("%x"))
        myDict ['d'] = x.strftime("%x")
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
            print("Termine")
            #self.otroContrato()
            self.disconnect()# ESTA DEBERIA ESTAR AQUI COSA QUE REGRESA AL MAIN(), tambien se desconecto de TWS Y DEBERIA COMENZAR DESPUES DEL app.run()
        else:
            print("Faltan lineas para terminar")   

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
        #global app
        print("Tratando de Implementar otro contrato")
        #contratos()
        # self.cancelMktData(0)
        app.cancelMktData(0)
        self.disconnect()
        subtractContratos() 
        newContrato()
        #self.disconnect()
        #main()
        #self.disconnect()
        #return
        
           
def main():
    #time.sleep(3)
    global myList
    global app
    global var1
    global var2
    app = TestApp()
    app.connect("127.0.0.1", 7497, 0)
    print("serverVersion:%s connectionTime:%s" % (app.serverVersion(),app.twsConnectionTime()))
    
    time.sleep(3)
    
    contract = Contract()
    contract.symbol = var2                #variable 2
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"
    contract.primaryExchange = var1     #variable 1 

    # contract = Contract()
    # contract.symbol = "AAPL"
    # contract.secType = "STK"
    # contract.exchange = "SMART"
    # Contract.currency = "USD"
    # contract.primaryExchange = "NASDAQ"


        #Esto son metodos de la clase EClient
    app.reqMarketDataType(4) # Este 4 es para delayed-frozen data
                
                #(tickrId, contract, genericTickList(GenericTickTypes), snapshot, regulatorySnaphsot,mkdDataOptions)
    app.reqMktData(0,contract,"",False,False,[])
    app.run()
    print("Existen mas contratos ???")
    newContrato()##SI NO HAY MAS CONTRATOS REGRESA A LA SIGUIENTE LINEA Y SI HAY LA FUNCION LO MANDARA DIRECTO AL main()
    ##ESTA FUNCION LUEGO DE EJECUTAR REGRESA A LA SIGUIENTE LINEA Y SI HAY UN CONTRATO PENDIENTE LA FUNCION LO MANDARA DIRECTO AL main()
    
    #app.disconnect()##NO ENCUENTRA ESTE  OBJETO
    #del app

def contratos():
    global myList
    global var1
    global var2
    myList = []
    print("Todos los contratos")
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
        print("Asigno Posicion")	
        var1 = myList[0]
        var2 = myList[1]
        print(myList)
        print("Termine el bucle de for y lectura del archivo.txt / Tengo un array de contratos")

# def subtractContratos():
#     global myList
#     global var1
#     global var2
#     myList.remove(myList[0])
#     myList.remove(myList[0])
#     var1 = myList[0]
#     var2 = myList[1]
#     print(myList)
#     if len(myList) == 0:
#         print("Termine")
#         app.disconnect()
#         return 
#     else:
#         print("Faltan Contratos para terminar")   

def newContrato():
    global app
    global var1
    global var2 
    global myList
    print("Se supone que elimine conexion del objeto anterior de la clase TestApp que es global")
    myList.remove(myList[0])
    myList.remove(myList[0])
    
    if len(myList) == 0:
        print("Termine todos los contratos")
        #app1.disconnect()##ESTE ESTARIA BIEN ESO CREO
        #exitContratos()
        #sys.exit(1)
        sys.exit()
        #quit()
        #exit(0)
        print("Llego a pasar por el returnnnn ???" )
        return #ESTE ES EL QUE ME REGRESA A "otroContrato"##SI FUNCIONA PARA EL REGRESO A LA OTRA FUNCION
        print("Pase por el return")
    else:
        print("Faltan contratos")
        print("Asigno posiciones")
    var1 = myList[0]
    var2 = myList[1]
    print(myList)
    main()
    print("No deberia pasar por aqui si funciona el if")
    
contratos()
main()
    