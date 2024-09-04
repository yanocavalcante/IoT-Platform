import pyproj

lat=-27.60171566
lng=-48.52081776
alt = 1

print(f"Latitude: {lat}; Longitude: {lng}; Altitude: {alt}")

transformer = pyproj.Transformer.from_crs(
        {"proj":'latlong', "ellps":'WGS84', "datum":'WGS84'},
        {"proj":'geocent', "ellps":'WGS84', "datum":'WGS84'}
        )

# Geographical to Geodesical
x, y, z =  transformer.transform( lng, lat, alt )

print(f"X: {x}; Y: {y}, Z: {z}")