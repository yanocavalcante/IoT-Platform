import time
import pandas as pd
import requests
import json
import pyproj
import pandas as pd


# CURRENT_TIME = int(time.time() * 1000000)
# lng=-48.52081776
# lat=-27.60171566

df = pd.read_csv('new_spotter.csv')
URL ='https://iot.lisha.ufsc.br/api/put.php'
CURRENT_TIME = time.time() * 1000000


for index, row in df.iloc[0:].iterrows():
    print(f"Reading Line {index}")
    time_epoch = row['GPS_Epoch_Time(s)']
    lat_degree = row['lat_degree_decimal']
    long_degree = row['long_degree_decimal']
    
    alt=1
    unidade = 0x84925924 #tempo (segundos)
    new_time_epoch = time_epoch * 1000000

    print(f"Lat_degree: {lat_degree}; Long_degree: {long_degree}")
    

    transformer = pyproj.Transformer.from_crs(
            {"proj":'latlong', "ellps":'WGS84', "datum":'WGS84'},
            {"proj":'geocent', "ellps":'WGS84', "datum":'WGS84'}
            )

    x, y, z =  transformer.transform( long_degree, lat_degree, alt )

    print(f"X: {x}; Y: {y}, Z: {z}")
    print(f"Time in Miliseconds Epoch: {new_time_epoch}")

    query = {
    "smartdata":[
        {
            "version": "1.2",
            "unit":unidade,
            "value":CURRENT_TIME,
            "error":0,
            "confidence":1,
            "x":x,
            "y":y,
            "z":z,
            "r":9000000,
            "t":new_time_epoch,
            "dev":1,
            "signature": 1,
            "workflow":0
        }
    ]
    }

    session = requests.Session()
    session.headers = {'Content-type' : 'application/json'}
    session.cert = ('../labeco.crt', '../labeco.key')
    requests.urllib3.disable_warnings()
    response = session.post(URL, json.dumps(query), verify=False)

    print("Get [", str(response.status_code), "] (", len(query), ") ", query, sep='')
    if response.status_code == 200:
        print(response.content)
    break