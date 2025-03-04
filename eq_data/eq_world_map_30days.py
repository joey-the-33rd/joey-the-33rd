from pathlib import Path
import json
import plotly.express as px

# Read the data as a string and convert to a python object.
path = Path('eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# Create a more relable version of the data file.
path = Path('eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)
print(readable_contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

# Display the count of recorded earthquakes in past 24 hrs.
print(len(all_eq_dicts))

# Extract the earthquake magnitudes and location.
mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']

    # Populate the lists with data from the file.
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

# Display the first 10 earthquake magnitudes, latitudes, 
# and logitudes using slices [:10], [:5], [:5] respectively.
print(mags[:10])
print(lons[:5])
print(lats[:5])

# Build a World Map with the earthquake data.
title = 'Global Earthquakes\n30 Days Record'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, 
                     title=title,
                     color=mags,
                     color_continuous_scale='viridis',
                     labels={'color':'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles,
                     )

# Display the map.
fig.show()



