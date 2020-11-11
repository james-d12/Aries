from PyQt5.QtWidgets import QToolBar, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QFileInfo
from gui.InputDialog import InputDialog

from data.Download import Download
from gui.Messages import errorMessageBox

class ToolBar(QToolBar):
    def __init__(self, parent):
        super(ToolBar, self).__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.downloadButton = QAction('Exit', self)
        self.downloadButton.setIcon(QIcon(QFileInfo(__file__).absolutePath()+"/img/download.png"))
        self.downloadButton.triggered.connect(self.downloadModPrompt)
        self.downloadButton.setToolTip("Download a Mod")
        self.addAction(self.downloadButton)


    def downloadModPrompt(self):
        input = InputDialog(None, "Download a Mod", "Enter Mod URL: ").input 
        download = Download(input)
        download.getInfo()

        if download.valid == True:
            self.parent.addDownload(download)
        else:
            errorMessageBox("Mod Download Warning", "Could not download the mod with the provided URL: {url}!".format(url=download.url))
        
