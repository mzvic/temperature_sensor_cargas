import os
import glob

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_folder1 = glob.glob(base_dir + '28*')[1]

device_file = device_folder + '/w1_slave'
device_file1 = device_folder1 + '/w1_slave'

def read_temp():
    with open(device_file, 'r') as f:
        while True:
            lines = f.readlines()
            if lines[0].strip()[-3:] == 'YES':
                break
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2:]
            temp_c = float(temp_string) / 1000.0
            return temp_c

def read_temp1():
    with open(device_file1, 'r') as f:
        while True:
            lines = f.readlines()
            if lines[0].strip()[-3:] == 'YES':
                break
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2:]
            temp_c = float(temp_string) / 1000.0
            return temp_c
