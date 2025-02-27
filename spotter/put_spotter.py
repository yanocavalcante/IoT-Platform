import pandas as pd
import requests, json, pyproj, os, time
from dotenv import load_dotenv


load_dotenv(dotenv_path="../.env",
            verbose=True,
            override=True)

URL = os.getenv('URL') + "/api/put.php"

df = pd.read_csv('new_spotter.csv')
CURRENT_TIME = time.time() * 1000000


for index, row in df.iloc[0:].iterrows():
    # print(f"Reading Line {index}")
    time_epoch = row['GPS_Epoch_Time(s)']
    lat_degree = row['lat_degree_decimal']
    long_degree = row['long_degree_decimal']
    
    alt=1
    unidade = 0x84925924
    new_time_epoch = time_epoch * 1000000    

    transformer = pyproj.Transformer.from_crs(
            {"proj":'latlong', "ellps":'WGS84', "datum":'WGS84'},
            {"proj":'geocent', "ellps":'WGS84', "datum":'WGS84'}
            )

    x, y, z =  transformer.transform( long_degree, lat_degree, alt )

    x = int(x)
    y = int(y)
    z = int(z)

    # print(f"Time in Miliseconds Epoch: {new_time_epoch}")

    query = {
    "smartdata":[
        {
            "version": "1.2",
            "unit":unidade,
            "value":1,
            "error":0,
            "confidence":1,
            "x":x,
            "y":y,
            "z":z,
            "r":0,
            "t":new_time_epoch,
            "dev":1,
            "signature": "BL0001",
            "workflow":0
        }
    ]
    }

    session = requests.Session()
    session.headers = {'Content-type' : 'application/json'}
    session.cert = ('../labeco.crt', '../labeco.key')
    requests.urllib3.disable_warnings()
    response = session.post(URL, json.dumps(query), verify=False)

    print("HTTP ", str(response.status_code), " (", len(query), ") ", query, sep='')

    print("Response:", response.content)

    break
