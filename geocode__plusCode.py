import pandas as pd
import geocoder
from openlocationcode import openlocationcode as pluscode
import pygeohash

# Input file

# Use your CSV file as input
df=pd.read_csv("Untitled spreadsheet - Jammu and Kashmir.csv") 



df['latitude'] = None
df['longitude'] = None
df['geohash'] = None
df['pluscode'] = None


for index, row in df.iterrows():
    i,j,k = row["statename"], row["Districtname"], row["officename"]
    g = geocoder.arcgis(f"India {i} {j} {k} ")

    latitude = g.latlng[0]
    longitude = g.latlng[1]

    ghash = pygeohash.encode(latitude, longitude)

    pc = pluscode.encode(latitude, longitude)

    print(f"{index} {k} {latitude}, {longitude}, {pc}, {ghash}")

    df.at[index, 'latitude'] = latitude
    df.at[index, 'longitude'] = longitude
    df.at[index, 'geohash'] = ghash
    df.at[index, 'pluscode'] = pc

# Output file
df.to_csv('modified_data_jammu_kashmir.csv')