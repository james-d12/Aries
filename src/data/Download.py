from requests.auth import HTTPBasicAuth
import requests
import json

from data.Utility import extractGameFromURL, extractIDFromURL

class Download:
    def __init__(self, url):
        self.game = extractGameFromURL(url)
        self.modID = extractIDFromURL(url)
        self.url = url 

    def getInfo(self, apikey):
        url = ("https://api.nexusmods.com/v1/games/{game}/mods/{modID}/files.json".format(game=self.game, modID=self.modID))
        fileInfoJson = requests.get(url=url, headers=apikey).json()
        for k in fileInfoJson:
            if k == "files":
                for j in fileInfoJson[k]:
                    for k2 in j:
                        if k2 == "file_id":
                            self.fileID = j[k2]
                            self.fileURL = ("https://api.nexusmods.com/v1/games/skyrimspecialedition/mods/{modID}/files/{fileID}.json".format(modID=self.modID, fileID=self.fileID))

    def print(self):
        print("     Game: ", self.game)
        print("     Mod ID: ", self.modID)
        print("     File ID: ", str(self.fileID))
        print("     File URL: ", self.fileURL)