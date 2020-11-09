from PyQt5.QtWidgets import QWidget, QInputDialog

class InputDialog(QWidget):
    def __init__(self, parent=None, name="", prompt=""):
        super(InputDialog, self).__init__(parent) 
        self.name = name
        self.prompt = prompt
        self.input = ""
        self.initUI()

    def initUI(self):
        text, ok = QInputDialog.getText(self, self.name, self.prompt)
        if ok:
            self.input = text 

    