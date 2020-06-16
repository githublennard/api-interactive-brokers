# Python program to read 
# file word by word 

import re
global var1
global var2
global myList
myList = [] # Lista Vacia
myValor = [] # Lista Vacia

with open('paraLeer1.txt','r') as file: #Este tiene coma en el texto 
	# reading each line	 
	for line in file:
		#for word in line.split(",",1):
		#for word in line.split(',|\n|\s',1):
		#for word in line.split(','):	
		for word in line.split():	
			print(word)
			myList.append(word)
		# print(re.split(',|\n',line)) 
		# print(re.split(',',line)) 
		# print(re.split(',|\s',line)) 
		# print(re.split(',',line))
	print(myList)
print("Termino Ejemplo")
print(','.join(myList))
s= (','.join(myList))
print("Valor de S:")
print(s)
for valor in s.split(','):
	print(valor)
	myValor.append(valor)

print("Lista Final")
print(myValor)


