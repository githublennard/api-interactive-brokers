import argparse

global myList
myList = []
# create the top-level parser  ## LOS COMANDO DE ESTE NIVEL SON PRIORIDAD AL MOMENTO DE SER LLAMADOS
parser = argparse.ArgumentParser(description = "Parameters for my Program to deply the API IB")

#parser.add_argument('DESCARGA', nargs='+')##ESTE ES UN POSITIONAL ARGUMENTS

# create subcommands ## CREO DIFERENTES SUBCOMANDOS
subparsers = parser.add_subparsers(help='commands for the API IB')

# A Download command
downloads_parser = subparsers.add_parser('DOWNLOADS', help='Download all the Financial Instruments')#CREANDO EL OBJETO
#downloads_parser.add_argument('INSTRUMENTS',action='store',nargs='*', help='All the Financial Instruments')
#downloads_parser.add_argument('INSTRUMENTS',nargs='*', action='store', help='All the Financial Instruments')##PUEDO OMITIR ESTE Y SI EL TAMAÑO ES = 1 ACTIVO LA FUNCION

#downloads_parser.set_defaults(func=INSTRUMENTS)
#parser.add_argument('DOWNLOADS', nargs='+')##ESTE ES UN POSITIONAL ARGUMENTS

# A List command
list_parser = subparsers.add_parser('LIST', help='List all the Financial Instruments')
list_parser.add_argument('MARKETS', action='store', nargs='*',help='All the Financial Instruments')##El * captura de cero a mas argumentos
#list_parser.add_argument('MARKETS', action='store', nargs='+',help='All the Financial Instruments')
#list_parser.add_argument('MERCADITOS', action='store', help='All the Financial Instruments')

#list_parser.add_argument('dirname', action='store', help='Directory to list')
#list_parser.add_argument('mercado', action='store', help='Directory to list')


# A ADD command
adding_parser = subparsers.add_parser('ADD', help='Add Financial Instruement')

# adding_parser.add_argument('MARKET', action='store',nargs='*', help='Market Name to add')
# adding_parser.add_argument('FINANCIAL_INSTRUMENT', action='store',nargs='*', help='Name Instrument')

adding_parser.add_argument('MARKET', action='store', help='Market Name to add')
adding_parser.add_argument('FINANCIAL_INSTRUMENT', action='store', help='Name Instrument')

# A DEL command
del_parser = subparsers.add_parser('DEL', help='Deleted Financial Instruement')
del_parser.add_argument('MARKET', action='store', help='Market Name to deleted')
del_parser.add_argument('FINANCIAL_INSTRUMENT', action='store', help='Name Instrument')
del_parser.add_argument('--read-only', default=False, action='store_true',
                           help='Set permissions to prevent writing to the directory',
                           )

args = parser.parse_args()

#print (parser.parse_args())

for _, value in parser.parse_args()._get_kwargs():
	if value is not None:
		myList.append(value)
		#print(value)
		#print(value)
		#myList.append(value)
print(myList)
print(len(myList))
print(str(myList))
#print(args.list)