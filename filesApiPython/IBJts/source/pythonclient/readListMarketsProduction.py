# Python program to read 
# file word by word 

global myList
myList = [] # Lista Vacia
finalList = [] # Lista Vacia

with open('paraLeer.txt','r') as file: #Este tiene coma en el texto 
	# reading each line	 
	for line in file:
		for word in line.split():	
			#print(word)
			myList.append(word)
print("List Financial Instruments Available: ['MARKET,STOCK','MARKET,STOCK','MARKET,STOCK'....] ")
print(myList)

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


