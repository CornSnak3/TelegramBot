import os
import paramiko
from dotenv import load_dotenv
from pathlib import Path


class LinuxConnector:
    def __init__(self):
        dotenvPath = Path("conf/ssh.env")
        load_dotenv(dotenv_path=dotenvPath)
        self.host = os.getenv("HOST")
        self.port = os.getenv("PORT")
        self.username = os.getenv("USER")
        self.password = os.getenv("PASSWORD")

    def connectorExec(self, command):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=self.host, username=self.username, password=self.password, port=self.port)
        stdin, stdout, stderr = client.exec_command(command=command)
        data = stdout.read() + stderr.read()
        client.close()
        data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
        return data
