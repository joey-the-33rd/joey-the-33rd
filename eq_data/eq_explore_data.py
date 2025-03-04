from pathlib import Path
import json
import plotly.express as px

# Read the data as a string and convert to a python object.
path = Path('eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# Create a more relable version of the data file.
path = Path('eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

# Display the count of recorded earthquakes in past 24 hrs.
print(len(all_eq_dicts))

# Extract the earthquake magnitudes and location.
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]

    # Populate the lists with data from the file.
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Display the first 10 earthquake magnitudes, latitudes, 
# and logitudes using slices [:10], [:5], [:5] respectively.
print(mags[:10])
print(lons[:5])
print(lats[:5])

# Build a World Map with the earthquake data.
title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, title=title)
fig.show()



