#!/usr/bin/env python3
import time
import requests
import json
import sys
import os
import pyproj

# Execupado apenas uma vez, na criacao de cada boia.


lng =  -48.52081776
lat = -27.60171566
alt = 12

raio = 1000*1000 #1000km
unidade = 0x84925924 #tempo (segundos)
URL ='https://iot.ufsc.br/api/create.php'
INICIO=1718766826
FIM=2034310424
transformer = pyproj.Transformer.from_crs({"proj":'latlong', "ellps":'WGS84', "datum":'WGS84'},{"proj":'geocent', "ellps":'WGS84', "datum":'WGS84'})
x, y, z =  transformer.transform( lng, lat, alt)
query = {
   "series":
      {
         "version": "1.2",
         "unit": unidade,
         "x": x,
         "y": y,
         "z": z,
         "r": raio,
         "t0": INICIO * 1000000,
         "tf": FIM * 1000000,
         "dev": 1,
         "signature": 1,
      }
}

session = requests.Session()
session.headers = {'Content-type' : 'application/json'}
session.cert = ['labeco.crt', 'labeco.key']
requests.urllib3.disable_warnings()

response = session.post(URL, json.dumps(query), verify=False)

print("Get [", str(response.status_code), "] (", len(query), ") ", query, sep='')
#print( str(response.content.decode('utf-8')) )

if response.status_code == 200:
    print(response.content)
