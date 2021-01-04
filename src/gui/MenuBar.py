from PyQt5.QtWidgets import QMenuBar, qApp, QMenu
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from gui.Menu import MenuActionCreate, MenuCreate
from gui.settings.SettingsMenu import * 

class MenuBar(QMenuBar):
    def __init__(self, parent):
        super(MenuBar, self).__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.settings = SettingsMenu()
        self.menuQuit = MenuActionCreate(self.parent, '&Exit', "Exit Application", qApp.quit)
        self.menuRefresh = MenuActionCreate(self.parent, '&Refresh', "Refresh Application", self.parent.update)
        self.fileMenu = MenuCreate(self.parent.menuBar(), '&File')
        self.fileMenu.addAction(self.menuRefresh)
        self.fileMenu.addAction(self.menuQuit)

        self.optionsMenu = MenuActionCreate(self.parent, '&Options', "View Options", self.showSettingsMenu)
        self.settingsMenu = MenuCreate(self.parent.menuBar(), '&Settings', self.optionsMenu)

    def showSettingsMenu(self):
        self.settings.show()
