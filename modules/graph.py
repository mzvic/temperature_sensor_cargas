import matplotlib.pyplot as plt
from datetime import datetime
import re

def parse_temperature_data(data):
    """
    Parse timestamp and temperature values from the given data.

    Parameters:
    - data: String containing timestamp and temperature values.

    Returns:
    - Tuple of two lists: timestamps and temperature values.
    """
    timestamps = []
    temperatures_0 = []
    temperatures_1 = []

    # Regular expression to extract data from the input string
    pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+); DS18B20_0: (\d+\.\d+); DS18B20_1: (\d+\.\d+)')

    matches = re.finditer(pattern, data)

    for match in matches:
        timestamp = match.group(1)
        temperature_0 = float(match.group(2))
        temperature_1 = float(match.group(3))

        timestamps.append(datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f'))
        temperatures_0.append(temperature_0)
        temperatures_1.append(temperature_1)

    return timestamps, temperatures_0, temperatures_1

def plot_temperature_data(timestamps, temperatures_0, temperatures_1):
    """
    Plot temperature data in a Cartesian coordinate system.

    Parameters:
    - timestamps: List of datetime objects representing timestamps.
    - temperatures_0: List of temperature values for DS18B20_0.
    - temperatures_1: List of temperature values for DS18B20_1.
    """
    plt.plot(timestamps, temperatures_0, label='DS18B20_0')
    plt.plot(timestamps, temperatures_1, label='DS18B20_1')

    plt.xlabel('Timestamp')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Data')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example data
data = """2023-11-15 13:04:31.016071; DS18B20_0: 23.062; DS18B20_1: 22.562
2023-11-15 13:04:32.616152; DS18B20_0: 23.0; DS18B20_1: 22.562
2023-11-15 13:04:34.280109; DS18B20_0: 23.0; DS18B20_1: 22.625"""

# Parse data
timestamps, temperatures_0, temperatures_1 = parse_temperature_data(data)

# Plot data
plot_temperature_data(timestamps, temperatures_0, temperatures_1)



csv_file_path = '2023-11-15 13:03:34.490869.csv'
timestamps, temperatures_0, temperatures_1 = parse_temperature_data(csv_file_path)
plot_temperature_data(timestamps, temperatures_0, temperatures_1)
