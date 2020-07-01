import argparse
global myArgsList
myArgsList = []

def downloadsFichero (args):
    print("Funcion descargar instrumentos del Fichero")

def listFichero (args):
    print("Funcion para leer Fichero")

def addFichero (args):
    print("Funcion para agregar instrumentos al Fichero")
    print(myAddList)

def delFichero (args):
    print("Funcion para eliminar instrumentos del Fichero")
    print(myDelList)


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

print(args.scmd)

myAddList = []
myDelList = []
if args.scmd == "DOWNLOADS":##El atributo de args se guarda en el destino 'scmd',se compara y si cumple se ejecuta algo
    downloadsFichero(args)
elif args.scmd == "LIST":
    listFichero(args)
elif args.scmd == "ADD":
    myAddList.append(args.MARKET)##Si mando a imprimir lo que esta dentro de () 
    myAddList.append(args.FINANCIAL_INSTRUMENT)
    print(myAddList)
    addFichero(args)
elif args.scmd == "DEL":
    myDelList.append(args.MARKET)
    myDelList.append(args.FINANCIAL_INSTRUMENT)
    print(myDelList)
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
