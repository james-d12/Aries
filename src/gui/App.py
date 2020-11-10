from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QFileInfo
from PyQt5.QtGui import QIcon

import qtmodern.styles

class App(QApplication):
    def __init__(self, left=200, top=200, width=1200, height=800):
        super(App, self).__init__([])
        self.setApplicationName("Aries")
        self.setApplicationVersion("0.1")
        self.setApplicationDisplayName("Aries")
        self.setWindowIcon(QIcon(QFileInfo(__file__).absolutePath()+'/img/icon-32x32.png'))


    def setThemeLight(self):
        qtmodern.styles.light(self)

    def setThemeDark(self):
        qtmodern.styles.dark(self)
