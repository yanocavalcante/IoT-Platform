import pandas as pd
import requests, json, pyproj, os, time
from dotenv import load_dotenv


load_dotenv(dotenv_path="../.env",
            verbose=True,
            override=True)

URL = os.getenv('URL') + "/api/put.php"

METERS = 0x84964924
SECONDS = 0x84925924
DEGREES =  0xF8000000

ALT = 1


def insert_data(timestamp, wv_height, pk_period, mn_direction, lat, long):
    print("Inserting Data...")

    timestamp = timestamp * 1000000
    transformer = pyproj.Transformer.from_crs(
            {"proj":'latlong', "ellps":'WGS84', "datum":'WGS84'},
            {"proj":'geocent', "ellps":'WGS84', "datum":'WGS84'}
            )

    x, y, z =  transformer.transform(long, lat, ALT)

    data = {
        "MultiUnitSmartData": {
        "version": "1.2",
        "x": int(x),
        "y": int(y),
        "z": int(z),
        "t0": int(timestamp),
        "signature": "BL0001",
        "series": [
            {   
                "unit": METERS,
                "value": wv_height,
                "dev": 1,
            }, {
                "unit": SECONDS,
                "value": pk_period,
                "dev": 2,
            }, {
                "unit": DEGREES,
                "value": mn_direction,
                "dev": 3,
            }
        ]
    }}

    session = requests.Session()
    session.headers = {'Content-type' : 'application/json'}
    session.cert = ('../labeco.crt', '../labeco.key')

    requests.urllib3.disable_warnings()
    json_data = json.dumps(data)

    response = session.post(URL, json_data, verify=False)

    print("HTTP [", str(response.status_code), "] (", len(data), ") ", json_data, sep='')
    print(response.text)


if __name__ == "__main__":
    
    df = pd.read_csv('acc.csv')
    for index, row in df.iloc[0:].iterrows():
        print(f"Reading Line {index}")

        time_epoch = int(row["Epoch_Time"])
        wv_height = float(row["Wave_Height"])
        pk_period = float(row["Peak_Period"])
        mn_direction = float(row["Mean_Direction"])
        lat = float(row["Lat"])
        long = float(row["Long"])
        insert_data(time_epoch, wv_height, pk_period, mn_direction, lat, long)

        time.sleep(2)