# Python program to read 
# file word by word 

#EN ESTE CODIGO VOY LEER UN ARCHIVO TXT PARA FORMAR UNA LISTA DE CONTRATOS QUE ME SIRVE PARA ASIGNAR 'MERCADO,ACCION' EN OTRA 
#FUNCION COMO VARIABLES

global myList
myList = [] # Lista Vacia
finalList = [] # Lista Vacia

with open('paraLeer1.txt','r') as file: #Este tiene coma en el texto 
	# reading each line	 
	for line in file:
		for word in line.split():	
			print(word)
			myList.append(word)
	print("Lista Previa: ")
	print(myList)
print("Uniendo los elementos en la lista")
print(','.join(myList))
s = (','.join(myList))#Juntando todo los elementos en una variable
print("Valor de S:")
print(s)
for elemento in s.split(','):
	print(elemento)
	finalList.append(elemento)

print("Lista Final para Contratos")
print(finalList)


