import paramiko
import re
import time
from Paloalto.Cut.Interfaces.interface import identify_interface




def get_asa_config(hostname, username, password, output_file, ssh):
    try:
        ssh.connect(hostname=hostname, username=username, password=password, timeout=10)
        print(f"Connected to {hostname} with {username} ")
        ssh_shell = ssh.invoke_shell()
        while not ssh_shell.recv_ready():
            pass
        ssh_shell.send("enable\n")
        time.sleep(1)
        ssh_shell.send("Ex@pr0be!\n")
        time.sleep(1)
        ssh_shell.send("terminal pager 0\n") 
        time.sleep(1)
        print(f"Show running-config ")
        ssh_shell.send("show running-config\n")
        print(f"configuration reading")
        time.sleep(5)
        
        start_pattern = re.compile(r': Saved')
        end_pattern = re.compile(r': end')  
        
        output = ''
        is_started = False
        while True:
            time.sleep(1)
            if ssh_shell.recv_ready():
                received_output = ssh_shell.recv(65535).decode('utf-8')
                output += received_output
                if not is_started:
                    match_start = start_pattern.search(output)
                    if match_start:
                        is_started = True
                        output = output[match_start.start():]  
                    
                match_end = end_pattern.search(output)
                if match_end:
                    output = output[:match_end.end()]  
                    break

        output = output.replace('\n', '')
 
        
        
        with open(output_file, 'w') as file:
            file.write(output)
            
        
        print(f"La configuration de l'ASA a été sauvegardée dans {output_file}")
        identify_interface(output_file)
        

    except paramiko.AuthenticationException:
        print("Auth Failed")
    except paramiko.SSHException as e:
        print(f"Erreur SSH: {str(e)}")
    finally:
        ssh.close()