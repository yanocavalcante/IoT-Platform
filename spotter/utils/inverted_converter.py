import pyproj

# x = 1234567.89
# y = 2345678.90
# z = 3456789.01

x =  3746442.252982531
y = -4237684.203724253
z = -2937463.928875127

print(f"X: {x}; Y: {y}, Z: {z}")

transformer = pyproj.Transformer.from_crs(
    {"proj": 'latlong', "ellps": 'WGS84', "datum": 'WGS84'},
    {"proj": 'geocent', "ellps": 'WGS84', "datum": 'WGS84'}
)

# Geodesical to Geographical
long_degree, lat_degree, alt = transformer.transform(x, y, z, direction='INVERSE')

print(f"Latitude: {lat_degree}; Longitude: {long_degree}; Altitude: {alt}")
