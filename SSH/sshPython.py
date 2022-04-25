#Connect to a remote file server via SSH and schedule file transfers. 
#Source: https://www.youtube.com/watch?v=6a8OimVvTEs&ab_channel=PracticalPythonSolutions-ByPaulMahon

import paramiko 
import sys
import time

results = []
hostIP = ''
username = ''
password = ''

def ssh_conn():
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect(hostIP, username, password)

    commands = ['mkdir Desktop/Test','ls -l']

    for command in commands: 

        ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command(command)
        time.sleep(.5)
        print(ssh_stdout.read().decode())

    

    for line in ssh_stdout: 
        results.append(line.strip('\n'))

ssh_conn()

for i in results:
    print(i.strip())

sys.exit()