#!/usr/bin/env python3

import requests
import json
import urllib3

from pprint import pprint

requests.packages.urllib3.disable_warnings()

url= "http://www.mapquestapi.com/directions/v2/route?key=AGRVT98WynBY3tQur6DtGJM6I1JC4bB7&from=madrid&to=zaragoza"


#Estableciendo las cabeceras// Que sea un diccionario
headers = {

    'Content-Type':'application/json'
}

#variable que almacena la respuesta de la peticion que se hace
                        #cabecera   #en este parentesis indicamos todo lo que  lleva la peticion
resp = requests.get(url,headers=headers,verify=False)

#variable 
print("La peticion tiene el estado",resp.status_code)

#Esta es una variable que indica que la variable "resp" me la devuelva en formato "json" 
response_json = resp.json()

#print(response_json)

#libreria para tener una vista mas limpia al capturar datos y verlos impreso en pantalla
#pprint(response_json)

#Aqui se parsea la respuesta, es decir devuelve lo que que te indico en los "[]", se obtiene un resultado mas exacto
print("La distancia es:",response_json['route']['distance'],"km")

#Para usar esta opcion se hace un casting, se modifica el tipo de solicitud que se hace
pprint("La distancia es:" +str( response_json['route']['distance'])+"km")



