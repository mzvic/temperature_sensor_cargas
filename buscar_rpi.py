import ipaddress
from ping3 import ping
import paramiko

def ping_and_ssh(start_ip, end_ip, ssh_username, ssh_password):
    start = ipaddress.IPv4Address(start_ip)
    end = ipaddress.IPv4Address(end_ip)

    for ip_int in range(int(start), int(end) + 1):
        current_ip = ipaddress.IPv4Address(ip_int)
        ip_str = str(current_ip)

        # Ping
        response = ping(ip_str, timeout=1)
        if response is not None:
            print(f"{ip_str} is reachable (Round-trip time: {response} ms)")

            # Attempt SSH connection
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                # Disable strict host key checking (use only in a trusted network)
                ssh.load_system_host_keys()
                ssh.connect(ip_str, username=ssh_username, password=ssh_password, allow_agent=False, look_for_keys=False)

                # Perform any actions you need with the SSH connection here

                print(f"La Raspberry está ubicada en: {ip_str}")
                ssh.close()
                return ip_str
                quit()
            except paramiko.AuthenticationException:
                print(f"Authentication failed for {ip_str}")
            except paramiko.SSHException as e:
                print(f"Unable to establish SSH connection to {ip_str}: {str(e)}")
            except Exception as e:
                print(f"Error connecting to {ip_str}: {str(e)}")
        else:
            #print(f"{ip_str} is not reachable")
            pass
	
if __name__ == "__main__":
    start_ip = "192.168.0.100"
    end_ip = "192.168.0.200"
    ssh_username = "raspy"
    ssh_password = "raspy"

    ping_and_ssh(start_ip, end_ip, ssh_username, ssh_password)
