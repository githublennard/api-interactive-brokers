# Python program to read 
# file word by word 

global myList
global myAddList
myList = [] # Lista Vacia
myAddList = ['NASDAQ','ACCION3']
print(myAddList[0])
print(myAddList[1])
with open('paraLeer1.txt', 'a+') as f:
	f.write('\n'+"%s,%s" % ((myAddList[0]),(myAddList[1])))
	
with open('paraLeer1.txt','r') as file: #Este tiene coma en el texto 
	# reading each line	 
	for line in file:
		for word in line.split():	
			#print(word)
			myList.append(word)
print("List Financial Instruments Available: ['MARKET,STOCK','MARKET,STOCK','MARKET,STOCK'....] ")
print(myList)


# # def processTickLine(self):
# # 	global contador
# # 	print("GENERANDO FICHERO")
# # 	x = datetime.datetime.now()
# # 	print(x.strftime("%x"))
# # 	myDict ['d'] = x.strftime("%x")
# # 	with open(('./DATOS/%s/%s.txt' % (var1,var2)), 'a+') as f:
# # 		f.write("%s,%2.2f,%2.2f,%2.2f,%2.2f,%i" % ((myDict['d']),
# # 												(myDict['68']),
# # 												(myDict['72']),
# # 												(myDict['73']),
# # 												(myDict['75']),
# # 												(myDict['74'])) + '\n')
# # 	print("Pasando Por Contador")
# # 	contador -= 1
# # 	print(contador)
# # 	if contador == 0:
# # 		print("Termine con un contrato de la lista")
# # 		#self.otroContrato()
# # 		self.disconnect()# Manda al codigo a la linea despues de app.run()
# # 	else:
# # 		print("Faltan lineas para terminar")   





