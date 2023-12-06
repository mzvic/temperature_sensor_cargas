from datetime import datetime
import paramiko
from buscar_rpi import *
import os
import sys
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.load_system_host_keys()

start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # date -s

if len(sys.argv) == 2:
    try:
        ip_str = "192.168.0." + str(sys.argv[1])
        ssh.connect(ip_str, username="raspy", password="raspy", allow_agent=False, look_for_keys=False)
    except:
        print("No se ha podido conectar con la Raspberry Pi")
        sys.exit()
else:
    ip_str = ping_and_ssh("192.168.0.100" , "192.168.0.200", "raspy", "raspy")
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
