from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from data.NexusKey import NexusKey


class NexusMenu(QWidget):
    def __init__(self, parent=None):
        super(NexusMenu, self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        self.layout = QGridLayout()


        self.keyLabel = QLabel("Nexus Key")
        self.keyText = QLineEdit()
        self.keyText.setEchoMode(QLineEdit.Password)

        vspacer = QSpacerItem(QSizePolicy.Minimum, QSizePolicy.Expanding)
        hspacer = QSpacerItem(QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout.addWidget(self.keyLabel, 0, 0)
        self.layout.addWidget(self.keyText, 0, 1)
        self.layout.addItem(hspacer, 0, 2, -1, 1)
        self.layout.addItem(vspacer, 2, 0, 1, -1)


        self.setLayout(self.layout)

