# Python program to read 
# file word by word 

import re
global var1
global var2
global myList
myList = [] # Lista
# opening the text file 
with open('paraLeer.txt','r') as file: #Este tiene espacios
	# reading each line	 
	for line in file: 
		# reading each word		 
		#for word in line.split(",",1): #Si hago esplit de 1 me devuelve una lista de 2 elementos
		for word in line.split(): #Con el separador de espacio por defecto me devuelve lo que necesito
		#for word in line.split('[, \n]'): #Con el separador de espacio por defecto me devuelve lo que necesito
		#for word in line.split(",|\n| |"): #Con el separador de espacio por defecto me devuelve lo que necesito
		#for word in line.split(',|;|',file): #Con el separador de espacio por defecto me devuelve lo que necesito
			# displaying the words		 
			print(word)
			myList.append(word)
			
		print("Termine leer linea")
	# print("Asigno Posicion")	
	# var1 = myList[0]
	# var2 = myList[1]
	print(myList)
	
