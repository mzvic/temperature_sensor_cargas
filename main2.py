from datetime import datetime
import paramiko
from buscar_rpi import *

def change_remote_date(ip_address, username, password):
    try:
        # Set up SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.load_system_host_keys()

        # Connect to the Raspberry Pi
        ssh.connect(ip_address, username=username, password=password, allow_agent=False, look_for_keys=False)

        # Get the current date and time
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Change the date on the Raspberry Pi
        stdin, stdout, stderr = ssh.exec_command("sudo date -s '{}'".format(str(start_time)))
        stdout_str = stdout.read().decode()
        stderr_str = stderr.read().decode()
        print("Remote date after change:", stdout_str)
        print("Error (if any):", stderr_str)


    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the SSH connection in a finally block to ensure it gets closed even if an exception occurs
        if ssh:
            ssh.close()

if __name__ == "__main__":
    # Replace these values with your actual Raspberry Pi credentials and IP address
    raspberry_pi_ip = "192.168.0.128"
    raspberry_pi_username = "raspy"
    raspberry_pi_password = "raspy"

    try:
        # Find Raspberry Pi IP address
        ip_str = ping_and_ssh(raspberry_pi_ip, "192.168.0.200", raspberry_pi_username, raspberry_pi_password)

        if ip_str:
            # Change the remote date
            change_remote_date(ip_str, raspberry_pi_username, raspberry_pi_password)
        else:
            print("Error: Unable to find the Raspberry Pi's IP address.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

