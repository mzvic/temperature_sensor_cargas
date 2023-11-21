
# Temperature Sensor Code
This code is specifically crafted for the CARGAS LLAMA project. It is designed to interface with two DS18B20 sensors connected to a Raspberry Pi 4. The program provides real-time readings of date, time, and temperatures from the sensors. Additionally, the output is saved in a CSV file named with the corresponding date and time.

#  Usage (Laboratory Setting)
Make sure to connect to the same Wifi that the Raspberry is connected (Cepia_work_5). <br />
<br />
Connect to the Raspberry Pi through SSH using the following command:
`ssh raspy@192.168.0.101`
The pasword is: `raspy`

Execute the script:
`$ sh script.sh`<br />
It will asks for the date and hour, then it shows and output with this format:
`<date and hour>, DS18B20: <temperature>, DS18B20_1: <temperature>`

To stop reading and writing, press `Ctrl + C`. The data will be uploaded to the [DATOS](https://github.com/mzvic/temperature_sensor_cargas/tree/main/DATOS) folder.

To visualize the output graphically, run the following command using the graph.py script:<br />
`python graph.py DATOS/data_to_graph.csv`<br />
<br />
Make sure to replace DATOS/data_to_graph.csv with the actual path to the CSV file containing the data you want to graph.

# GPIO Connections 
In case of any disconnection with the Raspberry, follow this table:
|DS18B20| Raspberry Pi |
|--|--|
| (Red Cable) VCC | Pin 1 (3.3V) |
| (Grey Cable) GND| Pin 6 (GND) |
| (Orange Cable) Data| Pin 7 (GPIO 4) |
<br/>

[Example of connection](https://imgur.com/a/WS1oDGb.jpeg)

# Dependencies
- buscar_rpi.py requires: ping3, paramiko (pip install ping3 paramiko)
- graph.py requires: matplotlib (pip install matplotlib)

# Reference Documentation
1.  **DS18B20 Temperature Sensor Documentation:**
    
    -   [DS18B20 Datasheet](https://datasheets.maximintegrated.com/en/ds/DS18B20.pdf): The official datasheet from Maxim Integrated provides detailed technical specifications and usage guidelines for the DS18B20 temperature sensor.
2.  **GPIO Pinout for Raspberry Pi 4:**
    
    -   [Raspberry Pi GPIO Pinout](https://pinout.xyz/): Pinout.xyz is a useful resource that provides information about the GPIO pinout for various Raspberry Pi models.
