from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

try:
    path = Path('weather_data/sitka_weather_2021_simple-original.csv')
    lines = path.read_text().splitlines()

    reader = csv.reader(lines)
    header_row = next(reader)

    # Get the dates and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    # Plot the high and low temperatures.
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, color='red', label='High')
    ax.plot(dates, lows, color='blue', label='Low')

    # Format plot.
    ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperatures (F)", fontsize=16)
    ax.tick_params(labelsize=16)
    ax.legend()

    # Show plot
    plt.show()

except FileNotFoundError:
    print("Weather data file not found.")
except IndexError:
    print("Error reading data from CSV file.")