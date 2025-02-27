#!/usr/bin/env python3
import requests, json, pyproj, os
from dotenv import load_dotenv


load_dotenv(dotenv_path="../.env",
            verbose=True,
            override=True)

URL = os.getenv('URL') + "/api/create.php"

LNG =  -48.52081776
LAT = -27.60171566
ALT = 1

RADIUS = 1000*1000

BEGIN=1718766826
END=2034310424

METERS = 0x84964924
SECONDS = 0x84925924
DEGREES =  0xF8000000

UNITS = [METERS, SECONDS, DEGREES]

transformer = pyproj.Transformer.from_crs({"proj":'latlong', "ellps":'WGS84', "datum":'WGS84'},{"proj":'geocent', "ellps":'WGS84', "datum":'WGS84'})
x, y, z =  transformer.transform(LNG, LAT, ALT)


for i in range(len(UNITS)):
   series = {
      "series":
         {
            "version": "1.2",
            "unit": UNITS[i],
            "x": int(x),
            "y": int(y),
            "z": int(z),
            "r": RADIUS,
            "t0": BEGIN * 1000000,
            "tf": END * 1000000,
            "dev": i+1,
            "signature": "BL0001",
         }
   }

   session = requests.Session()
   session.headers = {'Content-type' : 'application/json'}
   session.cert = ('../labeco.crt', '../labeco.key')

   response = session.post(URL, json.dumps(series))

   print("HTTP ", str(response.status_code), " (", len(series), ") ", series, sep='')

   print("Response:", response.content)