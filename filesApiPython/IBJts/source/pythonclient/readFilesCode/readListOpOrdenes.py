# Python program to read 
# file word by word 
###ESTA ES LA VERSION QUE USOS PARA LA LECTURA DE LAS ORDENES
global myList
myList = [] # Lista Vacia
finalList = [] # Lista Vacia

with open('ordenes.txt','r') as file: #Este tiene coma en el texto 
	# reading each line	 
	for line in file:
		#for word in line.split(" ",2):
		for word in line.split():		
			#print(word)
			myList.append(word)
print("LIST OF ALL ORDERS TO EXECUTE: ")
while (len(myList) > 0) :
	print(myList[0:6])#Comienza desde Cero pero no toma el 6
	del myList[0:6] 
	 


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


