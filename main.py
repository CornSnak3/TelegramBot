import logging
import requests

import  linux_connector, bot_connector

def main():
    connectorLinux = linux_connector.LinuxConnector()
    print(connectorLinux.connectorExec("lsb_release -a"))
    connectorBot = bot_connector.BotConnector()


if __name__ == "__main__":
    main()
