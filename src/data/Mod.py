from requests.auth import HTTPBasicAuth
import requests
import json

from data.Utility import extractGameFromURL, extractIDFromURL
from data.NexusAPI import requestMod

class Mod:
    def __init__(self, url):
        self.game = extractGameFromURL(url)
        self.modID = extractIDFromURL(url)
        self.link = url 

    def getInfo(self):
        modInfoJson = requestMod(self.game, self.modID)

        self.name = modInfoJson["name"]
        self.author = modInfoJson["author"]
        self.version = modInfoJson["version"]
        self.ID = modInfoJson["mod_id"]

    def print(self):
        print("Name: ", self.name)
        print("     Mod Author: ", self.author)
        print("     Mod Version: ", str(self.version))
        print("     Mod ID: ", str(self.ID))


