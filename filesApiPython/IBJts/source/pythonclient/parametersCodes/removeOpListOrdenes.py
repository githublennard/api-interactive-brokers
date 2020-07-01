# Python program to read 
# file word by word 
###ESTA ES LA VERSION QUE USOS PARA LA LECTURA DE LAS ORDENES Y BORRAR ORDENES
global myList
myList = [] # Lista Vacia
finalList = [] # Lista Vacia
finalListAnul = []
with open('ordenes.txt','r') as file: #Este tiene coma en el texto 
	for line in file:# reading each line	 
		for word in line.split():		
			#print(word)
			myList.append(word)
print(myList)
print("Tamaño Lista")
print(len(myList))
var1 = "1"
print("valor de var1: ")
print(var1)
print("\n")

while len(myList) > 0 :
	print("Primer elemento de la lista: ")
	print(myList[0])
	if myList[0] != var1 :
		 finalList.append(myList[0:6])
		 #print("Guardo la orden")
		 del myList[0:6]
		 #print(finalList)
	else:
		del myList[0:6]
		print("Borro la orden y el tamaño que queda es: ")
		#print(len(myList))
		#print(myList[0])

print("\n")
print("Lista con ordenes anuladas: ")
print(finalList)
print("Tamaño de la lista contenedora: ")
print(len(finalList))
print("Tamaño de una lista dentro de la lista contenedora: ")
print(len(finalList[0]))
print("Elementos de una lista dentro de la lista contenedora: ")
print(finalList[0])

while len(finalList) > 0:
	for elemento in finalList[0]:
		#print("elemento que se va a una lista: ")
		finalListAnul.append(elemento) #elemento que se va a una lista
		#print(elemento)
	del finalList[0]#Eliminamos una lista 

	# for posicion in finalList[0]:
	# 	print("Posicion")
	# 	finalListAnul.append(posicion)
	# 	print(posicion)
print("print finalListAnul: ")
print(finalListAnul)


while len(finalListAnul) > 0:
	print("Funcion para agregar Ordenes al Fichero")
	#print(finalListAnul)
	with open('ordenesRemove.txt', 'a+') as f:
			f.write('\n'+"%d %s %s %s %d %2.2f" %  (int(finalListAnul[0]),
												   (finalListAnul[1]),
											       (finalListAnul[2]),
												   (finalListAnul[3]),
												   int(finalListAnul[4]),
												   float(finalListAnul[5])))#Momento en el que escribe en el archivo.txt
	del finalListAnul[0:6]

# with open('ordenes.txt','r') as file: #Este tiene coma en el texto
# 	for line in file:# reading each line
# 		for word in line.split():
# 			myList.append(word)
# print(len(myList))
# print(myList)
# print("\n")
# print("LIST OF ALL ORDERS AFTER EXECUTED PARAMETER ADDOP: [ID,OPERATION,MARKET,STOCK,QUANTITY,MAX PRICE]"+"\n")
# while (len(myList) > 0) :
# 	print(myList[0:6])#Comienza desde Cero pero no toma el 6
# 	del myList[0:6]
#      sys.exit()


# print("Uniendo los elementos en la lista")
# print(','.join(myList))
# s = (','.join(myList))#Juntando todo los elementos en una variable
# print("Valor de S:")
# print(s)
# for elemento in s.split(','):
# 	print(elemento)
# 	finalList.append(elemento)

# print("Lista Final para Contratos")
# print(finalList)


# for elemento in finalList.split():
# 	print(elemento)
# 	tempList.append(elemento)

# print(tempList)

# print("Uniendo los elementos en la lista")
# print(','.join(finalList))
# s = (','.join(finalList))#Juntando todo los elementos en una variable
# print("Valor de S:")
# print(s)
# for elemento in s.split(','):
# 	print(elemento)
# 	finalList.append(elemento)

# print("Lista Final para Contratos")
# print(finalList)




## NO FUNCIONA YA QUE LO COPIA CON LLAVES [] Y COMAS
# with open('ordenesRemove.txt', 'a+') as f:
# 	f.write(str(finalList[0]))



# def addFicheroOp (args):
#     myList = [] # Lista Vacia
#     print("Funcion para agregar Ordenes al Fichero")
#     #print(finalListAnul)
#     with open('ordenesRemove.txt', 'a+') as f:
#         f.write('\n'+"%d %s %s %s %d %2.2f" %  (int(finalListAnul[0]),
#                                                 (finalListAnul[1]),
#                                                 (finalListAnul[2]),
#                                                 (finalListAnul[3]),
#                                                 int(finalListAnul[4]),
#                                                 float(finalListAnul[5])))#Momento en el que escribe en el archivo.txt

#     with open('ordenes.txt','r') as file: #Este tiene coma en el texto
#         for line in file:# reading each line
#             for word in line.split():
#                 myList.append(word)
#     print(len(myList))
#     print(myList)
#     print("\n")
#     print("LIST OF ALL ORDERS AFTER EXECUTED PARAMETER ADDOP: [ID,OPERATION,MARKET,STOCK,QUANTITY,MAX PRICE]"+"\n")
#     while (len(myList) > 0) :
#         print(myList[0:6])#Comienza desde Cero pero no toma el 6
#         del myList[0:6]
#     sys.exit()

#print(finalList)
# # # for elem in myList:
# # # 	#print(myList)
# # # 	if myList[0] == var1:
# # # 		del myList[0:6]
# # # 		print("Estoy en If")
# # # 		print(len(myList))
# # # 		print(myList[0])
# # # 		#continue
# # # 	else:
# # # 		finalList.append(myList[0:6])
# # # 		print("Estoy en else")
# # # 		del myList[0:6]
# # # 		print(finalList)


# for elem in myList:
# 	if myList[0] == var1:
# 		del myList[0:6]
# 		print(len(myList))
# 		print("Estoy en If")
# 		continue
	
# 	print(myList)


# # if myList[0] == var1:#Aqui deberia ir la variable del ID
# # 	print("Estoy en If")
# # 	del myList[0:6]
# # 	print(len(myList))
# # 	print(myList)
# # else:
# # 	print("Estoy en Else")
# # 	finalList.append(myList[0:6])
# # 	print(finalList[0:6])#Comienza desde Cero pero no toma el 6
# # 	del finalList[0:6] 

#print(myList)
	

# print("Uniendo los elementos en la lista")
# print(','.join(myList))
# s = (','.join(myList))#Juntando todo los elementos en una variable
# print("Valor de S:")
# print(s)
# for elemento in s.split(','):
# 	print(elemento)
# 	finalList.append(elemento)

# print("Lista Final para Contratos")
# print(finalList)


