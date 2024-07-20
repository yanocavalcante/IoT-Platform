#!/usr/bin/env python3
import time, requests, json

URL ='https://iot.lisha.ufsc.br/api/get.php'

unidade = 0x84925924 #tempo (segundos)


# busca os ultimos 5 minutos
# minutos = 30
# t0 = 1704380445 * 1000000   # 4 de Janeiro de 2024
t0 = 0
tf = time.time() * 1000000
query = {
        'series' : {
            'version' : "1.2",
            'unit'    : unidade,
            'x': 0,
            'y': 0,
            'z': 0,
            'r': 9000000,
            'signature': 1,
            'dev'     : 1,
            't0'      : t0,
            'tf'      : tf,
        }
}

session = requests.Session()
session.headers = {'Content-type' : 'application/json'}
session.cert = ('../labeco.crt', '../labeco.key')
requests.urllib3.disable_warnings()
response = session.post(URL, json.dumps(query), verify=False)

print("Get [", str(response.status_code), "] (", len(query), ") ", query, sep='')
if response.status_code == 200:
    print(json.dumps(response.json(), indent=4, sort_keys=False))
