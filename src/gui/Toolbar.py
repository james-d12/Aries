from PyQt5.QtWidgets import QToolBar, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QFileInfo
from gui.InputDialog import InputDialog

class ToolBar(QToolBar):
    def __init__(self, parent):
        super(ToolBar, self).__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.downloadButton = QAction('Exit', self)
        self.downloadButton.setIcon(QIcon(QFileInfo(__file__).absolutePath()+"/img/download.png"))
        #self.downloadButton.triggered.connect()
        self.downloadButton.setToolTip("Download a Mod")
        self.addAction(self.downloadButton)
