from PyQt5.QtWidgets import QMenuBar, qApp
from gui.Menu import MenuActionCreate, MenuCreate

class MenuBar(QMenuBar):
    def __init__(self, parent):
        super(MenuBar, self).__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.menuQuit = MenuActionCreate(self.parent, '&Exit', "Exit Application", qApp.quit)
        self.menuRefresh = MenuActionCreate(self.parent, '&Refresh', "Refresh Application", lambda : self.parent.update())
        self.fileMenu = MenuCreate(self.parent.menuBar(), '&File')
        self.fileMenu.addAction(self.menuRefresh)
        self.fileMenu.addAction(self.menuQuit)
        
        self.optionsMenu = MenuCreate(self.parent.menuBar(), '&Options')