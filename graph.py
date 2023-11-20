import csv
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.dates import DateFormatter
import sys

def plot_csv(filename):
    # Lists to store data
    timestamps = []
    values1 = []
    values2 = []

    # Read the CSV file
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            timestamp_str, value1_str, value2_str = row
            timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S.%f')
            value1 = float(value1_str)
            value2 = float(value2_str)
            timestamps.append(timestamp)
            values1.append(value1)
            values2.append(value2)

    # Plot the data
    plt.figure(figsize=(10, 6))

    plt.plot(timestamps, values1, label='Ambiente')
    plt.plot(timestamps, values2, label='Cargas')

    plt.xlabel('Timestamp')
    plt.ylabel('Temperature (°C)')
    plt.title('{}'.format(filename))
    plt.legend()
    plt.grid(True)
    plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d %H:%M:%S'))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename.csv>")
    else:
        filename = sys.argv[1]
        plot_csv(filename)
