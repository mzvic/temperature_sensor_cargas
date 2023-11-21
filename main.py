from modules.ds18b20 import *
from datetime import datetime
import os
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

import os
from datetime import datetime

start_time = datetime.now().isoformat()

def push():
    os.system("git add --all")
    os.system('git commit -m "{}"'.format(start_time))
    os.system("git push")

print("------------------------------")
import signal

def handler(signum, frame):
    print('Ctrl+Z pressed, but ignored')

signal.signal(signal.SIGTSTP, handler)
with open("./DATOS/" + str(start_time) + ".csv", 'w') as f:
    while True:
        try:
            ds18b20 = read_temp()
            ds18b20_1 = read_temp1()
            time_now = datetime.now()
            print("{}, DS18B20: {}, DS18B20_1: {}".format(time_now, str(ds18b20), str(ds18b20_1)))
            f.write("{}, {}, {}\n".format(time_now, str(ds18b20), str(ds18b20_1)))
            print("------------------------------")
        except KeyboardInterrupt:
            print("Nombre archivo: " + str(start_time))
            f.close()
            push()
            break
