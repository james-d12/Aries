from PyQt5.QtWidgets import QToolBar, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QFileInfo

from gui.InputDialog import InputDialog

import Data
from data.Mod import Mod

class ToolBar(QToolBar):
    def __init__(self, parent):
        super(ToolBar, self).__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        root = QFileInfo(__file__).absolutePath()


        downloadButton = QAction('Exit', self)
        downloadButton.setIcon(QIcon(root+"/download.png"))
        downloadButton.triggered.connect(self.downloadModPrompt)
        downloadButton.setToolTip("Download a Mod")
        self.addAction(downloadButton)

    def downloadModPrompt(self):
        modURL = InputDialog(None, "Mod URL", "Enter Mod URL: ").input 
        mod = Mod(modURL)
        mod.getInfo()
