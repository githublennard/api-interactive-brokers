import argparse
global myList
myList = []

def foo(args):
    print("descarga")

parser = argparse.ArgumentParser(description = "Parameters to deply the API IB")#Genero mi objeto

subparsers = parser.add_subparsers(title='Commands Available for the API IB',
                                    description='Each Commands has a diferent function',
                                    help='Execute each one separate')

# DOWNLOADS command
downloads_parser = subparsers.add_parser('DOWNLOADS',aliases=['co'], help='To download all the Financial Instruments')
downloads_parser.set_defaults(func=foo)
#list_parser.add_argument('dirname', action='store', help='Directory to list')
#list_parser.add_argument('mercado', action='store', help='Directory to list')

# A create command
create_parser = subparsers.add_parser('create', help='Create a directory')
create_parser.add_argument('dirname', action='store', help='New directory to create')
create_parser.add_argument('--read-only', default=False, action='store_true',
                           help='Set permissions to prevent writing to the directory',
                           )

# A delete command
delete_parser = subparsers.add_parser('delete', help='Remove a directory')
delete_parser.add_argument('dirname', action='store', help='The directory to remove')
delete_parser.add_argument('--recursive', '-r', default=False, action='store_true',
                           help='Remove the contents of the directory, too',
                           )

args = parser.parse_args()
#args1 = subparsers.parse_args()
myList = []
print("Debe imprimir valor de args")
print(args)  ##ESTO FUNCIONA--> Devuelve : Namespace(func=<function foo at 0x7fcbac56ed30>)
print("Debio imprimir valor de args")
args.func(args)##FUNCION PARA USAR args Y te llama a la funcion##SI LO HACE
print("funcion de args IMPRESA")

#if args.func()== "DOWNLOADS":
 #   print("ES UNA DESCARGA")

#if subparsers.add_parser == "DOWNLOADS":
 #   print("ES UNA DESCARGA")

print (parser.parse_args())
print(vars(args))

for _, value in parser.parse_args()._get_kwargs():
	if value is not None:
		myList.append(value)
print("PASANDO POR EL FOR y SIGUIENTE LINEA ES LA LISTA")
print( myList)
print(len(myList))

