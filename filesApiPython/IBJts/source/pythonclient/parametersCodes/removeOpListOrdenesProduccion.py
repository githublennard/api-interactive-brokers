
global myList
myList = [] # Lista Vacia
finalList = [] # Lista Vacia
finalListAnul = []
with open('ordenes.txt','r') as file: #Este tiene coma en el texto
	for line in file:# reading each line
		for word in line.split():
			#print(word)
			myList.append(word)
#print(myList)
print("Tamaño Lista")
print(len(myList))
var1 = "1"#ESTE ES EL ID QUE DEBE DE RECIBIR POR ARGPARSE
print("valor de var1: ")
print(var1)
print("\n")

while len(myList) > 0 :
	print("Primer elemento de la lista: ")
	print(myList[0])
	if myList[0] != var1 :
		 finalList.append(myList[0:6])
		 del myList[0:6]
	else:
		del myList[0:6]
		#print("Borro la orden y el tamaño que queda es: ")

print("\n")
print("Lista con ordenes anuladas: ")
print(finalList)
print("Tamaño de la lista contenedora: ")
print(len(finalList))
# print("Tamaño de una lista dentro de la lista contenedora: ")
# print(len(finalList[0]))
# print("Elementos de una lista dentro de la lista contenedora: ")
# print(finalList[0])

while len(finalList) > 0:
	for elemento in finalList[0]:
		#print("elemento que se va a una lista: ")
		finalListAnul.append(elemento) #elemento que se va a una lista
		#print(elemento)
	del finalList[0]#Eliminamos una lista

print("print finalListAnul: ")
print(finalListAnul)

while len(finalListAnul) > 0:
	#print("Funcion para agregar Ordenes al Fichero")
	#print(finalListAnul)
	with open('ordenesRemove.txt', 'a+') as f:
			f.write('\n'+"%d %s %s %s %d %2.2f" %  (int(finalListAnul[0]),
												   (finalListAnul[1]),
											       (finalListAnul[2]),
												   (finalListAnul[3]),
												   int(finalListAnul[4]),
												   float(finalListAnul[5])))#Momento en el que escribe en el archivo.txt
	del finalListAnul[0:6]

print("Was update order List")
