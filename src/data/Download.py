from requests.auth import HTTPBasicAuth
import requests
import json

from data.Utility import extractGameFromURL, extractIDFromURL
from data.NexusAPI import requestFilesForMod

class Download:
    def __init__(self, url):
        self.game = extractGameFromURL(url)
        self.modID = extractIDFromURL(url)
        self.url = url 

    def getInfo(self):
        fileInfoJson = requestFilesForMod(self.game, self.modID)
    
        for key in fileInfoJson["files"]:
            for key2 in j:
                if j["is_primary"] == True:
                    self.fileID = j["file_id"]
                    self.fileURL = ("https://api.nexusmods.com/v1/games/skyrimspecialedition/mods/{modID}/files/{fileID}.json".format(modID=self.modID, fileID=self.fileID))
                    break

    def print(self):
        print("     Game: ", self.game)
        print("     Mod ID: ", self.modID)
        print("     File ID: ", str(self.fileID))
        print("     File URL: ", self.fileURL)