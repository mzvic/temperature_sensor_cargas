from datetime import datetime
import paramiko
from buscar_rpi import *
import os
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.load_system_host_keys()

start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # date -s

ip_str = ping_and_ssh("192.168.0.128" , "192.168.0.200", "raspy", "raspy")

ssh.connect(ip_str, username="raspy", password="raspy", allow_agent=False, look_for_keys=False)

# Change the date on the Raspberry Pi
print("Cambiando fecha", end='\r')
start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
stdin, stdout, stderr = ssh.exec_command("sudo date -s '{}'".format(str(start_time)))
stdout_str = stdout.read().decode()
print("Fecha cambiada a:", stdout_str)

os.system("ssh raspy@{}".format(ip_str))

#TO DO: EJECUTAR MAIN.PY Y QUE SE VISUALICEN EN LA TERMINAL
ssh.close()
del stdin, stdout, stderr


