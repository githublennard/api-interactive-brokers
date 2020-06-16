from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum 
import datetime
import time
import sys
#ESTE MODELO FUNCIONA  PERO NO SALE DE UNA MANERA LIMPIA DE LA EJECUCION
#NO ES NECESARIO CREAR OTRO OBJETO PARA REUSAR LA CLASE TestApp
global myList
global app
global app1
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
        global app #revisar desde aqui
        global app1#revisar desde aqui
        global contador
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
            print("Termine escribir data Contrato")#Aqui podria eliminar ya los dos elementos
            #app.disconnect()##SI SURGE EFECTO DE NO CONEXION 
            #app1.disconnect()
            #del app # Creo que no hace efecto ya que es un objeto que esta dentro de la clase y deberia estar fuera, para borrarlo#NO FUNCIONA DA PROBLEMAS PORQUE ES UN OBJETO QUE ESTA FUERA DE LA CLASE Y NO DENTRO
            self.cancelMktData(0)#Como que funciona bien
            self.disconnect()#Como que funciona bien
            self.otroContrato()
            #self.disconnect()
            main()# Regresa a main() pero despues de la linea "app.run()" Probablemente -->> Se necesita return en otroContrato()
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
    
    def otroContrato(self):#Aqui no puedo instanciar un objeto de la clase TestApp ya que estoy dentro de la clase
        global app
        global app1   
        #self.cancelMktData(0)# A lo mejor cancela la peticion pero no me elimina el objeto de la clase y no me permite realizar conexiones
        #self.disconnect()#Cancelo Conexion para iniciar nueva conexion con otro objeto(importante)/Si no hago esto no funciona el codigo
        time.sleep(3)
        print("Tratando de Implementar otro contrato")#INTENTAR DE ELIMINAR AQUI ELEMENTOS Y VER SI PARA AQUI EL CODIGO
        while len(myList) > 0:
            #del app # Elimino objeto de la clase # No funciona lo toma como una variable local
            # myList.remove(myList[0])##Si podria eliminar aqui o en la funcion anterior
            # myList.remove(myList[0])
            print(myList)
            print("De aqui eliminare dos elementos de la lista")
            #self.main1()
            #return
            main1() #Aqui llamo a una funcion fuera de la clase y funciona
            self.disconnect()
            #app1.disconnect
            #main()            #ME GENERA UN BUCLE
        else:
            print("Termine el While de Lista")
            app.disconnect()
            app1.disconnect()
            exit()
            quit()
            self.cancelMktData(0)
            self.disconnect()
            #return #agregue este#No sirve--->> PROBAR ESTA  OPCION LUEGO
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
    print("Pasando por Run")#SOLO PASA AL INICIO
    app.run()
    print("Ver si paso por 'del app'")
    del app
    #app.disconnect()

def exitContratos():
    global app
    global app1
    print("Saliendo del Codigo")
    sys.exit(1)
    sys.exit()
    quit()
    exit(0)
    app.disconnect()
    app1.disconnect()
    
    

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
        #self.disconnect()#Da error el codigo  
        # app.disconnect()
        app1.disconnect()##ESTE ESTARIA BIEN ESO CREO
        # app.cancelMktData(0)
        # app1.cancelMktData(0)
        #del app# local variable 'app' referenced before assignment
        #del app1 #Que pasa si no borro este objeto##NADA EL CODIGO SIGUE CORRIENDO
        # sys.exit(1) #ME LLEVAN A OTRO SITIO
        # sys.exit()
        # quit()
        # exit(0)
        exitContratos()
        #return #ESTE ES EL QUE ME REGRESA A "otroContrato"##SI FUNCIONA PARA EL REGRESO A LA OTRA FUNCION

    var1 = myList[0]
    var2 = myList[1]
    

    print(myList)
    print("La lista que se muestra en pantalla ya tiene menos dos elementos")
    
    print("Se supone que voy a crear un nuevo contrato, por eso vuelvo a llamar a la clase,Inicio nueva conexion")
    app1 = TestApp()
    app1.connect("127.0.0.1", 7497, 0)
    time.sleep(3)
    contract = Contract()
    contract.symbol = var2                #variable 2
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"
    contract.primaryExchange = var1       #variable 1

    app1.reqMarketDataType(4)
    app1.reqMktData(0,contract,"",False,False,[])
    app1.run()
    app1.disconnect()##ESTA LINEA SE VE AFECTADA POR EL IF DE == 0 
    #self.disconnect() # self is not defined
    print("Termino el objeto de la clase app1")# Pasa por aqui luego de que termino todos los contratos, No deberia

    
main()
#main1()

# if __name__ == "__main__":
#      main()
    