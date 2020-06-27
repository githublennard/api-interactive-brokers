# Python program to read 
# file word by word 

#EN ESTE CODIGO VOY LEER UN ARCHIVO TXT PARA FORMAR UNA LISTA DE CONTRATOS QUE ME SIRVE PARA ASIGNAR 'MERCADO,ACCION' EN OTRA 
#FUNCION COMO VARIABLES

global myOrderList
myOrderList = [] # Lista Vacia
finalList = [] # Lista Vacia

with open('ordenes.txt','r') as file: #Este tiene coma en el texto 
	# reading each line	 
	for line in file:
		for word in line.split():	
			#print(word)
			myOrderList.append(word)
	print("Lista Previa: ")
	print(myOrderList)
print("Tengo una Lista con todas las ordenes")
print(len(myOrderList))
print(myOrderList[0])#Esta posicion siempre se ignora
print(myOrderList[1])

print("Variables a guardar y borrar: ")
#Estas 5 variables debe ser leidas del archivo ordenes.txt
varoOp = myOrderList[1]#"BUY"
varoVoSo = myOrderList[4]#150
varoMax = myOrderList[5]#361.20
varcSym = myOrderList[3]#"AAPL"
varcMer = myOrderList[2]#"ISLAND" #Se tiene que usar ISLAND en ves de "NASDAQ" 

del myOrderList[0:6]

print(varoOp)
print(varoVoSo)
print(varoMax)
print(varcSym)
print(varcMer)

#myOrderList.pop(0)
#myOrderList.pop(0:6)#NoFunciona
#myOrderList.pop(0)
print("Lista con ordenes por ejecutar: ")
print(len(myOrderList))
print(myOrderList)

# # print("Lista Final para Contratos")
# #         print(finalList)
# #         print("Asigno Posicion")	
# #         var1 = finalList[0]
# #         var2 = finalList[1]
# #         print(finalList)
# #         print("Termine el bucle de for y lectura del archivo.txt / Tengo un array de contratos")

# print("Uniendo los elementos en la lista")
# print(','.join(myOrderList))
# s = (','.join(myOrderList))#Juntando todo los elementos en una variable
# print("Valor de S:")
# print(s)
# for elemento in s.split(','):
# 	print(elemento)
# 	finalList.append(elemento)

# print("Lista Final para Contratos")
# print(finalList)


