import requests
import json
import Data

def __returnData(url):
        try: 
            return requests.get(url=url, headers=Data.apikey).json()
        except Exception:
            print("Error requesting data with URL: {url} from Nexus API.".format(url=url))
            return 

def __returnDataText(url):
    return json.dumps(__returnData(url))

def requestFilesForMod(game, modID):
    return __returnData(
        "https://api.nexusmods.com/v1/games/{game}/mods/{modID}/files.json".format(game=game,modID=modID))

def requestFileInfo(game, modID, fileID):
    return __returnData(
        "https://api.nexusmods.com/v1/games/{game}/mods/{modID}/files/{fileID}.json".format(game=game, modID=modID,fileID=fileID))

def requestDownloadLink(game, modID, fileID):
    return __returnData(
        "https://api.nexusmods.com/v1/games/{game}/mods/{modID}/files/{fileID}/download_link.json".format(game=game, modID=modID, fileID=fileID))
       
def requestMod(game, modID):
    return __returnData(
        "https://api.nexusmods.com/v1/games/{game}/mods/{modID}.json".format(game=game, modID=modID))

def requestModChangeLog(game, modID):
    return __returnData(
        "https://api.nexusmods.com/v1/games/{game}/mods/{modID}/changelogs.json".format(game=game, modID=modID))
