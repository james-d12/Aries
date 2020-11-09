from PyQt5.QtWidgets import QMessageBox

def messageBox(icon, title, text):
    errorMsg = QMessageBox()
    errorMsg.setIcon(icon)
    errorMsg.setWindowTitle(title)   
    errorMsg.setText(text)
    errorMsg.exec()

def infoMessageBox(title, text):
    messageBox(QMessageBox.Information, title, text)
def warningMessageBox(title, text):
    messageBox(QMessageBox.Warning, title, text)
def errorMessageBox(title, text):
    messageBox(QMessageBox.Critical, title, text)
