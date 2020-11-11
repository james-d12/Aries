from requests.auth import HTTPBasicAuth
import requests
import json

from data.Utility import extractGameFromURL, extractIDFromURL
from data.NexusAPI import requestMod

class Mod:
    def __init__(self, url):
        self.name = ""
        self.author = ""
        self.version = ""
        self.ID = ""
        self.game = extractGameFromURL(url)
        self.modID = extractIDFromURL(url)
        self.url = url 
        self.valid = True

    def getInfo(self):
        modInfoJson = requestMod(self.game, self.modID)

        try: 
            self.name = modInfoJson["name"]
            self.author = modInfoJson["author"]
            self.version = modInfoJson["version"]
            self.ID = modInfoJson["mod_id"]
        except Exception:
            print("Mod JSON data is invalid.")
            self.valid = False 


    def print(self):
        print("Name: ", self.name)
        print("     Mod Author: ", self.author)
        print("     Mod Version: ", str(self.version))
        print("     Mod ID: ", str(self.ID))


