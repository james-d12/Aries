from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class PathDirectoryInput(QWidget):
    def __init__(self, parent=None, label="", placeHolderText=""):
        super(PathDirectoryInput, self).__init__(parent)
        self.label = QLabel(label)
        self.text = QLineEdit(placeHolderText)
        self.text.setReadOnly(True)
        self.button = QPushButton("...")
        self.button.setFixedWidth(50)

    def setText(self, text):
        self.text.setText(text)
    def getText(self):
        return self.text.text()

class PathMenu(QWidget):
    def __init__(self, parent=None):
        super(PathMenu, self).__init__(parent)
        self.setWindowTitle("Path Settings")
        self.resize(400,200)
        self.initUI()

    def initUI(self):        
        self.layout = QGridLayout()

        self.folderInput = PathDirectoryInput(self, "Game Directory", "/")
        self.baseInput = PathDirectoryInput(self, "Base Directory", "/")
        self.downloadsInput = PathDirectoryInput(self, "Downloads Directory", "/downloads")
        self.modsInput = PathDirectoryInput(self, "Mods Directory", "/mods")
        self.pluginsInput = PathDirectoryInput(self, "Plugins Directory", "/plugins")

        self.folderInput.button.clicked.connect(self.setGameDirectory)
        self.baseInput.button.clicked.connect(self.setBaseDirectory)
        self.downloadsInput.button.clicked.connect(self.setDownloadDirectory)
        self.modsInput.button.clicked.connect(self.setModDirectory)
        self.pluginsInput.button.clicked.connect(self.setPluginDirectory)

        self.initWidgetsFromDirectoryInput(self.folderInput, 0)
        self.initWidgetsFromDirectoryInput(self.baseInput, 1)
        self.initWidgetsFromDirectoryInput(self.downloadsInput, 2)
        self.initWidgetsFromDirectoryInput(self.modsInput, 3)
        self.initWidgetsFromDirectoryInput(self.pluginsInput, 4)

        vspacer = QSpacerItem(QSizePolicy.Minimum, QSizePolicy.Expanding)
        hspacer = QSpacerItem(QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout.addItem(hspacer, 0, 2, -1, 1)
        self.layout.addItem(vspacer, 5, 0, 1, -1)

        self.setLayout(self.layout)

    def initWidgetsFromDirectoryInput(self, directoryInput, row):
        self.layout.addWidget(directoryInput.label, row, 0)
        self.layout.addWidget(directoryInput.text, row, 1)
        self.layout.addWidget(directoryInput.button, row, 2)

    def setGameDirectory(self):
        folder = QFileDialog.getExistingDirectory(self, 'Open Folder', 'c:\\')
        self.folderInput.text = folder
    def setBaseDirectory(self):
        folder = QFileDialog.getExistingDirectory(self, 'Open Folder', 'c:\\')
        self.baseInput.setText(folder)        
        self.downloadsInput.setText(folder+"/downloads/")
        self.modsInput.setText(folder+"/mods/")
        self.pluginsInput.setText(folder+"/plugins/")
    def setDownloadDirectory(self):
        folder = QFileDialog.getExistingDirectory(self, 'Open Folder', self.baseInput.getText())
        self.downloadsInput.setText(folder)
    def setModDirectory(self):
        folder = QFileDialog.getExistingDirectory(self, 'Open Folder', self.baseInput.getText())
        self.modsInput.setText(folder)
    def setPluginDirectory(self):
        folder = QFileDialog.getExistingDirectory(self, 'Open Folder', self.baseInput.getText())
        self.pluginsInput.setText(folder)

