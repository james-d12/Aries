from requests.auth import HTTPBasicAuth
import requests
import json
import wget

from data.Utility import extractGameFromURL, extractIDFromURL
from data.NexusAPI import requestFilesForMod, requestDownloadLink

class Download:
    def __init__(self, url):
        self.game = extractGameFromURL(url)
        self.modID = extractIDFromURL(url)
        self.url = url 
        self.fileName = ""
        self.fileID = ""
        self.fileURL = ""
        self.valid = False

    def getInfo(self):
        fileInfoJson = requestFilesForMod(self.game, self.modID)
        try:
            for key in fileInfoJson["files"]:
                for key2 in key:
                    if key["is_primary"] == True or key["category_name"] == "MAIN":
                        self.fileName = key["file_name"]
                        self.fileID = key["file_id"]
                        self.fileURL = ("https://api.nexusmods.com/v1/games/skyrimspecialedition/mods/{modID}/files/{fileID}.json".format(modID=self.modID, fileID=self.fileID))
                        self.valid = True
                        break 

        except Exception:
            print("Mod with requested URL could not be retrieved.")
                
    def download(self):
        data = requestDownloadLink(self.game, self.modID, self.fileID)

        for key in data:
            if (key["name"] == "Nexus Global Content Delivery Network"):
                url = key["URI"]
                data = requests.get(url, allow_redirects=True)
                self.downloadPath = '../downloads/{fileName}'.format(fileName=self.fileName)
                open(self.downloadPath, 'wb').write(data.content)

    def print(self):
        print("     Game: ", self.game)
        print("     Mod ID: ", self.modID)
        print("     File ID: ", str(self.fileID))
        print("     File URL: ", self.fileURL)