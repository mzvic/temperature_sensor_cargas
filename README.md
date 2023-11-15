# Temperature Sensor Code
This code is specifically crafted for the CARGAS LLAMA project. It is designed to interface with two DS18B20 sensors connected to a Raspberry Pi 4. The program provides real-time readings of date, time, and temperatures from the sensors. Additionally, the output is saved in a CSV file named with the corresponding date and time.

#  Usage (Laboratory Setting)
Connect to the Raspberry Pi through SSH using the following command:
`ssh raspy@192.168.0.118`
The pasword is: `raspy`

Execute the script:
`$ sh script.sh`
It will asks for the date and hour, then it shows and output with this format:
`<date and hour>, DS18B20: <temperature>, DS18B20_1: <temperature>`

To stop reading and writing, press `Ctrl + C`. The data will be uploaded to the [DATOS](https://github.com/mzvic/temperature_sensor_cargas/tree/main/DATOS) folder.

# GPIO Conections 
VCC --> Pin 1 (3.3V)
GND --> Pin 6 (GND)
DS18B20 --> Pin 7 (GPIO 4)
# Reference Documentation
1.  **DS18B20 Temperature Sensor Documentation:**
    
    -   [DS18B20 Datasheet](https://datasheets.maximintegrated.com/en/ds/DS18B20.pdf): The official datasheet from Maxim Integrated provides detailed technical specifications and usage guidelines for the DS18B20 temperature sensor.
2.  **GPIO Pinout for Raspberry Pi 4:**
    
    -   [Raspberry Pi GPIO Pinout](https://pinout.xyz/): Pinout.xyz is a useful resource that provides information about the GPIO pinout for various Raspberry Pi models.
