#!/usr/bin/env python3
import time, requests, os, json
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env",
            verbose=True,
            override=True)

URL = os.getenv('URL') + "/api/get.php"

METERS = 0x84964924
SECONDS = 0x84925924
DEGREES =  0xF8000000

UNITS = [METERS, SECONDS, DEGREES]
MEASUREMENTS = ['Hs', 'Tp', 'MwD']

t0 = 0
tf = time.time() * 1000000

dict_response = {'series':[]}

for i in range(len(UNITS)):
    query = {
            'series' : {
                'version': "1.2",
                'unit': UNITS[i],
                'x': 0,
                'y': 0,
                'z': 0,
                'r': 9000000,
                'signature': "BL0001",
                'dev': i+1,
                't0': int(0),
                'tf': int(tf),
            }
    }

    session = requests.Session()
    session.headers = {'Content-type' : 'application/json'}
    session.cert = ('../labeco.crt', '../labeco.key')
    requests.urllib3.disable_warnings()
    response = session.post(URL, json=query, verify=False)

    dict_temporary = json.loads(response.text)

    for j in range(len(dict_temporary['series'])):
        dict_temporary['series'][j][MEASUREMENTS[i]] = dict_temporary['series'][j].pop('value')
        
        if i == 0:
            dict_response.update(dict_temporary)
        else:
            dict_response['series'][j].update(dict_temporary['series'][j])

print(json.dumps(dict_response, indent=4))