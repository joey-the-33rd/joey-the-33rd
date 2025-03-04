from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path('Weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Print the index and value of each item in the 
# header row. 
#for index, column_header in enumerate(header_row):
#    print(index, column_header)

# Get the dates and high temparatures from this file.
dates, highs = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    dates.append(current_date)
    highs.append(high)

print(highs)

# Plot the high temparatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')

# Format plot.
ax.set_title("Daily high temparatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temparatures (F)", fontsize=16)
ax.tick_params(labelsize=16)

# Show plot
plt.show()
