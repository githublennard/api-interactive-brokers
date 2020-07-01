# Python program to read 
# file word by word 

#global myList
#global myAddList
myList = [] # Lista Vacia
myDelList = [] # Lista Vacia
# myAddList = ['NASDAQ','ACCION']
# print(myAddList[0])
# print(myAddList[1])
var1="NYSE"
var2="ABBV"
with open('paraLeer2.txt','r+') as file: #Este tiene coma en el texto 
	# reading each line	 
	for line in file:
		for word in line.split():#En este caso el espacio es el salto de linea
			print(word)
			if word != (var1+","+var2):#Este seria el "word"
				print("Este contrato se mantiene")
				myDelList.append(word)#Va colocando los contratos en una lista
				#del line
				print(myDelList)
				# with open('paraLeer2.txt','a+') as file:##Si funciona, pero lo comento no lo necesito por el momento
				# 	file.write(str(myDelList[-1])+'\n')   ##Si funciona, pero lo comento no lo necesito por el momento
	print("Lista con el contrato eliminado: ")
	print(myDelList)
	print(len(myDelList))
	#print(myDelList[0])
	contador = len(myDelList)

#AQUI GENERO UN NUEVO ARCHIVO.TXT DONDE, SE ABRA ELIMINADO UN CONTRATO	
with open('paraLeer2.txt','w+') as file:
	print("Inicio contador")
	while (contador != 0):
		file.write(str(myDelList[0])+'\n')
		myDelList.remove(myDelList[0])
		contador -= 1
		print(contador)
		print(myDelList)

	#file.writelines(myDelList)
	#file.writelines(str(myDelList[-1])+'\n')

# # 		file.write(value + '\n')
# # 		#file.write(str(myDelList[-1])+'\n')

# for value in myDelList:
# 	print(value)
# # for value in myDelList.split(","): #AttributeError: 'list' object has no attribute 'split'
# # 	with open('paraLeer3.txt','a+') as file:
# # 		file.write(value + '\n')
# # 		#file.write(str(myDelList[-1])+'\n')


##TODOO ESTO ES DE LECTURA PARA LIST, VEO LO QUE ME QUEDA DESPUES
with open('paraLeer2.txt','r') as file: #Este tiene coma en el texto 
	# reading each line	 
	for line in file:
		for word in line.split():	
			#print(word)
			myList.append(word)
print("List Financial Instruments Available: ['MARKET,STOCK','MARKET,STOCK','MARKET,STOCK'....] ")
print(myList)		





