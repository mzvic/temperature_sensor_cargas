from ds18b20 import *

from datetime import datetime
import os
import time
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

start_time = datetime.now()

with open("../DATOS/" + str(start_time) + ".txt", 'w') as f:
    while True:
        try:
            ds18b20 = read_temp()
            ds18b20_1 = read_temp1()
            time_now = datetime.now()
            print("[{}]".format(time_now))
            print("DS18B20: " + str(ds18b20))
            print("DS18B20_1: " + str(ds18b20_1))
            print("------------------------------")

            f.write("{}; DS18B20_0: {}; DS18B20_1: {}\n".format(time_now, str(ds18b20), str(ds18b20_1)))
        except KeyboardInterrupt:
            f.close()
