from SSH.ssh import ssh_connection
from Cisco_ASA.get_config import get_asa_config
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    ssh = ssh_connection()
    hostname = os.getenv('HOST')
    username = os.getenv('USER')
    password = os.getenv('PASSWORD')
    output_file = 'configuration_asa.txt'
    get_asa_config(hostname, username, password, output_file, ssh)


 

if __name__ == '__main__':
    main()
