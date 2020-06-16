# Python program to read 
# file word by word 

global var1
global var2
global myList
myList = [] # Lista
# opening the text file 
with open('paraLeer.txt','r') as file: 
	# reading each line	 
	for line in file: 
		# reading each word		 
		#for word in line.split(",",1): #Si hago esplit de 1 me devuelve una lista de 2 elementos
		for word in line.split(): #Con el separador de espacio por defecto me devuelve lo que necesito
			# displaying the words		 
			print(word)
			myList.append(word)
			
		print("Termine leer linea")
	print("Asigno Posicion")	
	var1 = myList[0]
	var2 = myList[1]
	print(myList)
	
print("En este momento deberia llamar al contrato y que haga el request de los precios" )
print("Regreso del request y tengo que borrar lo asignado previamente")

print("Intentando Definir Una nueva Funcion")

while len(myList) > 0:
	myList.remove(myList[0])
	myList.remove(myList[0])
	print(myList) 
else:
	print("Termine el While")

print("Final")

# 	for posicion in myList:
# 		if len(myList) > 0:   #SI ESTO SE CUMPLE PRODRIA EJECUTAR LA LLAMADA AL CONTRATO
# 			myList.remove(myList[0])
# 			myList.remove(myList[0])
# 		# else:                  #POR ALGUNA RAZON NO ME LEE ESTA SENTENCIA     
# 		# 	print("Paso por Else")
# 		#   	print(var1)
# 		#   	print(var2)	
# 	print("Imprimiendo datos ultimo contrato")
# print(myList) 
# print(var1)
# print(var2)

