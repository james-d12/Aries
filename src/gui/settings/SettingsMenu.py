from gui.settings.PathMenu import *
from gui.settings.NexusMenu import *
from PyQt5 import QtCore

class SettingsMenu(QWidget):
    def __init__(self, parent=None):
        super(SettingsMenu, self).__init__(parent)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.layout = QVBoxLayout(self)
        self.resize(600,400)

        self.tabs = QTabWidget()
        self.pathTab = PathMenu(self)
        self.nexusTab = NexusMenu(self)

        self.tabs.addTab(self.pathTab, "Path")
        self.tabs.addTab(self.nexusTab, "Nexus")
    
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        