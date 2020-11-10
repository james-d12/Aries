from PyQt5.QtWidgets import QMessageBox

def messageBox(icon, title, text):
    msgBox = QMessageBox()
    msgBox.setIcon(icon)
    msgBox.setWindowTitle(title)   
    msgBox.setText(text)
    msgBox.exec()

def infoMessageBox(title, text):
    messageBox(QMessageBox.Information, title, text)
def warningMessageBox(title, text):
    messageBox(QMessageBox.Warning, title, text)
def errorMessageBox(title, text):
    messageBox(QMessageBox.Critical, title, text)
