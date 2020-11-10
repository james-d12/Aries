from requests.auth import HTTPBasicAuth
from requests.exceptions import HTTPError, ConnectionError
import requests
import json
import os

from PyQt5.QtWidgets import QMessageBox
from gui.InputDialog import InputDialog
from gui.Messages import warningMessageBox

class NexusKey():
    def __init__(self):
        self.key = {}
        self.connected = False

    def writeKeyToFile(self):
        try:
            os.mkdir("config")
        except OSError:
            print("Could not create config directory.")

        with open("config/api-key.txt", 'w+') as file:
            file.write(self.key["apikey"])

    def readKeyFromFile(self):
        try:
            with open("config/api-key.txt", 'r') as file:
                self.key["apikey"] = file.readline()
        except FileNotFoundError as err:
            print(f"File error occured: {err}")
            self.key = {}

    def removeKeyFromFile(self):
        try:
            open("config/api-key.txt", 'w').close()
        except FileNotFoundError as err:
            print(f"File error occured: {err}")

    def doesKeyExist(self):
        try: 
            with open("config/api-key.txt", 'r') as file:
                file.seek(0) 
                char = file.readline() 
                if not char:
                    return False 
                return True
        except FileNotFoundError:
            return False

    def canConnect(self):
        try: 
            response = requests.get(url="https://api.nexusmods.com/", headers=self.key)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            return False
        except ConnectionError as connect_err:
            print(f'Connection error occurred: {connect_err}')
            return False
        except Exception as err:
            print(f'Other error occurred: {err}')
            return False
        else:
            print("Sucessfully connected to the Nexus Mods API!")
            return True 

    def process(self):
        if self.doesKeyExist():
            self.readKeyFromFile()    
            self.connected = self.canConnect()
            if not self.connected:
                self.removeKeyFromFile()
                self.key = {}
        else: 
            self.key["apikey"] = InputDialog(None, "API Key", "Enter Nexus API Key:").input
            self.connected = self.canConnect()
            if self.connected:
                self.writeKeyToFile()

    def connect(self):
        self.process()
        if not self.connected:
            warningMessageBox("Nexus API Connection Warning", "Cannot connect to Nexus Mods.")

