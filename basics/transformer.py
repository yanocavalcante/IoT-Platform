import pyproj
import pandas as pd


long_degree = -485607874 / 10000000  # Converter para graus
lat_degree = -274419587 / 10000000  # Converter para graus
alt = 0

print(long_degree)
transformer = pyproj.Transformer.from_crs(
        {"proj":'latlong', "ellps":'WGS84', "datum":'WGS84'},
        {"proj":'geocent', "ellps":'WGS84', "datum":'WGS84'}
        )

x, y, z =  transformer.transform( long_degree, lat_degree, alt )


print(x,y,z)