from requests.auth import HTTPBasicAuth
from requests.exceptions import HTTPError
import requests
import json

from data.NexusKey import NexusKey

class NexusAPI():
    def __init__(self):
        self.key = NexusKey() 

    def __returnData(self, url):
        try: 
            return requests.get(url=url, headers=self.key).json()
        except Exception:
            print("Error requesting data with URL:{url} from Nexus API.".format(url))

    def __returnDataText(self, url):
        return json.dumps(self.__returnData(url))

    def requestFilesForMod(self, game, modID):
        return self.__returnData(
            "https://api.nexusmods.com/v1/games/{game}/mods/{modID}/files.json".format(game=game,modID=modID))

    def requestFileInfo(self, game, modID, fileID):
        return self.__returnData(
            "https://api.nexusmods.com/v1/games/{game}/mods/{modID}/files/{fileID}.json".format(game=game, modID=modID,fileID=fileID))

    def requestDownloadLink(self, game, modID, fileID):
        return self.__returnData(
            "https://api.nexusmods.com/v1/games/{game}/mods/{modID}/files/{fileID}/download_link.json".format(game=game, modID=modID, fileID=fileID))
            
    def requestMod(self, game, modID):
        return self.__returnData(
            "https://api.nexusmods.com/v1/games/{game}/mods/{modID}.json".format(game=game, modID=modID))

    def requestModChangeLog(self, game, modID):
        return self.__returnData(
            "https://api.nexusmods.com/v1/games/{game}/mods/{modID}/changelogs.json".format(game=game, modID=modID))
