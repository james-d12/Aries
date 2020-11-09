from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QAction, QToolBar
from PyQt5.QtGui import QIcon

from PyQt5 import QtCore

from gui.Tables import ModTable, DownloadTable, PluginTable
from gui.MenuBar import MenuBar
from gui.InputDialog import InputDialog
from gui.Toolbar import ToolBar

from gui.Table import Table

class Window(QMainWindow):
    def __init__(self, left=200, top=200, width=1200, height=800):
        super(Window, self).__init__()
        self.setWindowTitle("Aries")
        self.setGeometry(left, top, width, height)
        self.initUI()

    def initMenuBar(self):
        self.menuBar = MenuBar(self)

    def initToolBar(self):
        self.toolBar = ToolBar(self)
        self.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)

    def initTable(self):   
        self.table = Table(self)
        self.setCentralWidget(self.table)

    def initUI(self):
        self.initMenuBar()
        self.initToolBar()
        self.initTable()

    def addMod(self, mod):
        self.table.addMod(mod)
    def addPlugin(self, plugin):
        self.table.addPlugin(plugin)
    def addDownload(self, download):
        self.table.addDownload(download)

    