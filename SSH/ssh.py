import paramiko

def ssh_connection():
    print("Connexion Attempt ...")
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    return ssh_client