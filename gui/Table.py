from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget

from gui.Tables import ModTable, DownloadTable, PluginTable
from gui.MenuBar import MenuBar
from gui.InputDialog import InputDialog

class Table(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        self.tabs = QTabWidget()
        self.modsTab = ModTable(self)
        self.rootModsTab = ModTable(self)
        self.downloadsTab = DownloadTable(self)
        self.pluginsTab = PluginTable(self)

        self.tabs.addTab(self.modsTab,"Mods")
        self.tabs.addTab(self.rootModsTab,"Root Mods")
        self.tabs.addTab(self.downloadsTab,"Downloads")
        self.tabs.addTab(self.pluginsTab,"Plugins")

        
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def addMod(self, mod):
        self.modsTab.addMod(mod)
    def addPlugin(self, plugin):
        self.pluginsTab.addPlugin(plugin)
    def addDownload(self, download):
        self.downloadsTab.addDownload(download)

    