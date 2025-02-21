#!/usr/bin/env python3
import requests, json, pyproj, os
from dotenv import load_dotenv


load_dotenv()

URL = os.getenv('URL') + "/api/create.php"

lng =  -48.52081776
lat = -27.60171566
alt = 12

raio = 1000*1000 #1000km
unidade = 0x84925924 #tempo (segundos)

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
         "signature": "BL0001",
      }
}

session = requests.Session()
session.headers = {'Content-type' : 'application/json'}
session.cert = ('../labeco.crt', '../labeco.key')

response = session.post(URL, json.dumps(query))

print("HTTP ", str(response.status_code), " (", len(query), ") ", query, sep='')

print("Response:", response.content)