from requests.auth import HTTPBasicAuth
import requests
import json

import Data

class Mod:
    def __init__(self, url):
        self.link = url
        url = url.replace("https://www.nexusmods.com/", "")
        self.url = ("https://api.nexusmods.com/v1/games/{modURL}".format(modURL = url))

    def getInfo(self):
        url = ("{url}.json".format(url = self.url))
        modInfoJson = requests.get(url=url, headers=Data.apikey).json()
        self.name = modInfoJson["name"]
        self.author = modInfoJson["author"]
        self.version = modInfoJson["version"]
        self.ID = modInfoJson["mod_id"]

    def print(self):
        print("{name}: ".format(name=self.name))
        print("     Mod Author: ", self.author)
        print("     Mod Version: ", str(self.version))
        print("     Mod ID: ", str(self.ID))
        self.downloadFile.print()


