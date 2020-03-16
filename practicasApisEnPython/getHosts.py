#!/usr/bin/env python3

import requests
import json
import urllib3
from pprint import pprint
from tabulate import * 


requests.packages.urllib3.disable_warnings()

url= "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/host"


#Estableciendo las cabeceras// Que sea un diccionario
headers = {

    'Content-Type' : 'application/json',
    'X-Auth-Token' : 'ST-2087-a9TBeEtCkSrJc5Co1Ynk-cas'
}

#body_json = {
 # "password": "Xj3BDqbU",
  #"username": "devnetuser"
#}

#variable que almacena la respuesta de la peticion que se hace
                        #cabecera   #en este parentesis indicamos todo lo que  lleva la peticion
#resp = requests.get(url,headers=headers,verify=False)

#json.dumps --> Serializacion (Convertirlo a json) // Esto se hace ya que estoy usando python pero el endpoint tiene json
#json.loads  --> .json  --> deserializar (Convertirlo a dictionary))

#resp = requests.post(url,json.dumps(body_json),headers=headers,verify=False)


resp = requests.get(url,headers=headers,verify=False)

hostList = []
 
print("La peticion tiene el estado",resp.status_code)

#Esta es una variable que indica que la variable "resp" me la devuelva en formato "json" 
response_json = resp.json()

#print(response_json)

counter = 0
for el in response_json['response']:
    counter+=1
    host = [
        counter,
        #response_json['response']
        el['hostType'],
        el['hostIp'],
        el['hostMac']   
    ]
    #append = Nos sirve para indicar que vamos a añadir algo en una variable por eso concatenamos
    hostList.append(host)
tableHeader = ["Number","Type","IP","MAC"] 

print(tabulate(hostList,tableHeader))
#libreria para tener una vista mas limpia al capturar datos y verlos impreso en pantalla
#pprint(response_json)

#print("El ticket de servicio es:",response_json['response']['serviceTicket'])

#Aqui se parsea la respuesta, es decir devuelve lo que que te indico en los "[]", se obtiene un resultado mas exacto
#print("La distancia es:",response_json['route']['distance'],"km")

#Para usar esta opcion se hace un casting, se modifica el tipo de solicitud que se hace
#pprint("La distancia es:" +str( response_json['route']['distance'])+"km")

#El hostname, pertenece a la familia <familia>, y su MAC es <MAC> y su version de IOS es <version>
#for equipo in response_json

###
#counter = 0
#for equipo in response_json['response']:
#    print("El hostname",response_json['response'][counter]['hostname'],"pertenece a la familia",response_json['response'][counter]['family'],
#    "su MAC es", response_json['response'][counter]['macAddress'],"y su version de IOS es:",response_json['response'][counter]['softwareVersion'])
#    counter +=1
###  
