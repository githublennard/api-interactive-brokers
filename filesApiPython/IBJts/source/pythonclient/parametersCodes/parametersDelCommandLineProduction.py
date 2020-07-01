import argparse
global myArgsList
myArgsList = []

def downloadsFichero (args):
    print("Funcion descargar instrumentos del Fichero")

def listFichero (args):
    print("Funcion para leer Fichero")

def addFichero (args):
    print("Funcion para agregar instrumentos al Fichero")
    #print(myAddList)
    print(var3)
    print(var4)
    global myList
    global myAddList1
    myList = [] # Lista Vacia
    myAddList1 = []#Los datos guardados en esta lista se usaran para escribir en el archivo .txt
    myAddList1.append(var3)
    myAddList1.append(var4)
    print(myAddList1)
    print(myAddList1[0])
    print(myAddList1[1])
    with open('paraLeer1.txt', 'a+') as f:
        f.write('\n'+"%s,%s" % ((myAddList1[0]),(myAddList1[1])))#Momento en el que escribe en el archivo.txt
        
    with open('paraLeer1.txt','r') as file: #Este tiene coma en el texto 
        # reading each line	 
        for line in file:
            for word in line.split():	
                #print(word)
                myList.append(word)
    print("List Financial Instruments Available: ['MARKET,STOCK','MARKET,STOCK','MARKET,STOCK'....] ")
    print(myList)
    print("Se agrego al final del array, el Instrumento Financiero")

def delFichero (args):
    global myDelList1
    myDelList1 = []#Los datos guardados en esta lista se usaran para escribir en el archivo .txt
    # myDelList1.append(var3)
    # myDelList1.append(var4)
    print(myDelList1)
    # print(myDelList1[0])
    # print(myDelList1[1])
    print("Funcion para eliminar instrumentos del Fichero")
    with open('paraLeer1.txt','r+') as file: #Este tiene coma en el texto 
        # reading each line	 
        for line in file:
            for word in line.split():
                print(word)
                if word != (var3+","+var4):
                    myDelList1.append(word)#Va colocando los contratos en una lista
                    print(myDelList)
        print("Lista con el contrato eliminado:")
        print(myDelList1)
        print(len(myDelList1))
        contador = len(myDelList1)

    with open('paraLeer1.txt','w+') as file:
        print("Inicio contador")
        while (contador != 0):
            file.write(str(myDelList1[0])+'\n')
            myDelList1.remove(myDelList1[0])
            contador -= 1
            print(contador)
            print(myDelList1)

parser = argparse.ArgumentParser(description = "Parameters to deply the API IB")#Genero mi objeto

subparsers = parser.add_subparsers(title='Commands Available for the API IB',
                                    description='Each Commands has a diferent function',
                                    dest= 'scmd',
                                    help='Execute each one separate')
                                    #En 'scmd' se guarda el atributo("nombre") de los subcomandos
                                    #Los 'args' son argumentos propios de cada subcomando 
# DOWNLOADS command
downloads_parser = subparsers.add_parser('DOWNLOADS', help='To download all the Financial Instruments')

# LIST command
list_parser = subparsers.add_parser('LIST', help='To list all the Financial Instruments')

# ADD command
adding_parser = subparsers.add_parser('ADD', help='Add Financial Instrument')
adding_parser.add_argument('MARKET', action='store', nargs=1, help='Market name to add')
adding_parser.add_argument('FINANCIAL_INSTRUMENT', action='store', nargs=1, help='Name Instrument')

# DEL command
del_parser = subparsers.add_parser('DEL', help='Deleted Financial Instrument')
del_parser.add_argument('MARKET', action='store', nargs=1, help='Market Name to deleted')
del_parser.add_argument('FINANCIAL_INSTRUMENT', action='store', nargs=1, help='Name Instrument')

args = parser.parse_args()

print(args.scmd)#Si coloco entre parentesis: 'args.MARKET' ; tambien lo imprime

myList = [] # Lista Vacia
myAddList = []
myDelList = []
if args.scmd == "DOWNLOADS":##El atributo de args se guarda en el destino 'scmd',se compara y si cumple se ejecuta algo
    downloadsFichero(args)
elif args.scmd == "LIST":
    listFichero(args)
elif args.scmd == "ADD":
    myAddList.append(args.MARKET)##Si mando a imprimir lo que esta dentro de () lo imprime
    myAddList.append(args.FINANCIAL_INSTRUMENT)
    print(myAddList) #Es una lista y cada elemento hay que sacarlo dos veces para solo tener el string
    #print(myAddList[0])
    #print(myAddList[1])
    var1 = myAddList[0]
    var2 = myAddList[1]
    print(var1)
    print(var2)
    #print(len(var1))
    var3 = var1[0].upper()#Me pone en mayuscula##Posicion Cero de 'var' porque son listas de un solo elemento
    var4 = var2[0].upper()#Aqui ya tengo el elemento en un string de caracteres que se llevaran a una lista nueva
    print(var3)#var3 y var4 seran los datos que se utilizaran en la otra funcion
    print(var4)
    addFichero(args)
elif args.scmd == "DEL":
    myDelList.append(args.MARKET)
    myDelList.append(args.FINANCIAL_INSTRUMENT)
    print(myDelList)
    var1 = myDelList[0]
    var2 = myDelList[1]
    print(var1)
    print(var2)
    var3 = var1[0].upper()#Me pone en mayuscula 
    var4 = var2[0].upper()#Aqui ya tengo el elemento en un string de caracteres que se llevaran a una lista nueva
    print(var3)#var3 y var4 seran los datos que se utilizaran en la otra funcion
    print(var4)
    delFichero(args)

print("Debe imprimir valor de args")
print(args)  ##ESTO FUNCIONA--> Devuelve : Namespace(func=<function foo at 0x7fcbac56ed30>)
#print(args.MARKET)##FUNCIONA, PODRIA UTILIZARLO PARA GRABAR DATOS EN UNA LISTA EN CASO SE NECESITE
print("Debio imprimir valor de args")

myArgsList = []
for _, value in parser.parse_args()._get_kwargs():
	if value is not None:
		myArgsList.append(value)
print("PASANDO POR EL FOR y SIGUIENTE LINEA ES LA LISTA DE ARGUMENTOS")
print(myArgsList)
print(len(myArgsList))
