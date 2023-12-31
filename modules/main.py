from dht22 import *
from ds18b20 import *
from relay import *
from turn_off_gpio import *

from datetime import datetime
import os
import time
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

extractor_on()

os.system("sh date.sh")


with open('data.txt', 'w') as f:
	while True:
		try:
			status_fan = False
			dht22_in = get_dht22_in()
			dht22_out = get_dht22_out()
			ds18b20 = read_temp()
			ds18b20_1 = read_temp1()
			time_now = datetime.now()

			try:
				
				if dht22_in.split(",")[0]>= 20 or ds18b20 >= 20 or ds18b20_1 >= 20:
						fan_on()
						status_fan = True
				else:
						fan_off()
						status_fan = False
				print("MODE 1")
			except (TypeError, AttributeError):
				
				if ds18b20 >= 20 or ds18b20_1 >= 20:
						fan_on()
						status_fan = True
				else:
						fan_off()
						status_fan = False 
			print("MODE 2")
			print("[{}]".format(time_now))
			print("DHT22 IN: " + str(dht22_in))
			print("DHT22 OUT: " + str(dht22_out))
			print("DS18B20: " + str(ds18b20))
			print("DS18B20_1: " + str(ds18b20_1))
			print("RELAY FAN: " + str(status_fan))
			print("-----------------------------")


			f.write("{}; DHT22 IN: {}; DHT22 OUT: {}; DS18B20_0: {}; DS18B20_1: {}; RELAY_FAN: {}\n".format(time_now, str(dht22_in), str(dht22_out), str(ds18b20), str(ds18b20_1), status_fan))
			

		except KeyboardInterrupt:
				f.close()
				turn_off_relay()
