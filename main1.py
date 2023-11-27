from datetime import datetime
import paramiko
from buscar_rpi import *

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.load_system_host_keys()

start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # date -s

ip_str = ping_and_ssh("192.168.0.100" , "192.168.0.200", "raspy", "raspy")

ssh.connect(ip_str, username="raspy", password="raspy", allow_agent=False, look_for_keys=False)


