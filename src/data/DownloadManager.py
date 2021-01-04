import requests, wget 
from data.Download import Download
from data.NexusAPI import requestDownloadLink

class DownloadManager:
    def __init__(self, downloadPath="../downloads/"):
        self.downloads = []
        self.downloadPath = downloadPath

    def addDownload(self, download):
        self.downloads.append(download)
        data = requestDownloadLink(self.game, self.modID, self.fileID)

        for key in data:
            if (key["name"] == "Nexus Global Content Delivery Network"):
                url = key["URI"]
                data = requests.get(url, allow_redirects=True)
                path = '{downloadPath}{fileName}'.format(downloadPath=self.downloadPath, fileName=download.fileName)
                with open(path, 'wb') as path: 
                    path.write(data.content)
    def addDownload(self, url):
        download = Download(url)
        self.addDownload(self, download)

    def removeDownload(self, download):
        self.downloads.remove(download)
    def removeAllDownloads(self):
        self.downloads = []
    def getDownloadLength(self):
        return len(self.downloads)
    