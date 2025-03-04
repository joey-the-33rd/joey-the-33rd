from pathlib import Path
import csv
from datetime import datetime
from matplotlib import pyplot as plt


path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

try:
    path = Path('weather_data/death_valley_2021_simple.csv')
    lines = path.read_text().splitlines()

    reader = csv.reader(lines)
    header_row = next(reader)

    # Get the dates and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        # The data file for Death Valley has missing adat
        # so we need to hundle the missing data.
        try:
            high = int(row[3])
            low = int(row[4])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # Plot the high and low temperatures.
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, color='red', label='High')
    ax.plot(dates, lows, color='blue', label='Low')

    # Format plot.
    title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA"
    ax.set_title(title, fontsize=20)
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