# Python program to read 
# file word by word 

import re
global var1
global var2
global myList
myList = [] # Lista Vacia

# f=open('paraLeer1.txt','r')
# for x in f:
# 	print(x)

f=open('paraLeer1.txt','r')
for linea in f:
	print(linea)
	print(re.split(",|''",linea))
	#print(re.split('; |, |\*|\n',linea))
	# for word in linea:
	# 	print(re.split('; |, |\*|\n',word))

