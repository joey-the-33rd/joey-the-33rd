import json

# File path
file_path = "eq_data/readable_eq_data.geojson"

# Read the GeoJSON file
with open(file_path, "r") as file:
    data = json.load(file)

# Extract the title from the metadata
title = data.get("metadata", {}).get("title", "No title found")

# Print the extracted title
print(title)
