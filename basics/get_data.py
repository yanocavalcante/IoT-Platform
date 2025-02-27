#!/usr/bin/env python3
import time, requests, os
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env",
            verbose=True,
            override=True)

URL = os.getenv('URL') + "/api/get.php"


METERS = 0x84964924
SECONDS = 0x84925924
DEGREES =  0xF8000000

t0 = 0
tf = time.time() * 1000000

query = {
        'series' : {
            'version': "1.2",
            'unit': DEGREES,
            'x': 0,
            'y': 0,
            'z': 0,
            'r': 9000000,
            'signature': "BL0001",
            'dev': 3,
            't0': int(1700000000000000),
            'tf': int(tf),
        }
}

session = requests.Session()
session.headers = {'Content-type' : 'application/json'}
session.cert = ('../labeco.crt', '../labeco.key')
requests.urllib3.disable_warnings()
response = session.post(URL, json=query, verify=False)

print("HTTP ", str(response.status_code), " (", len(query), ") ", query, sep='')

print("Response:", response.content)
