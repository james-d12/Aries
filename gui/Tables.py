from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QAbstractScrollArea

class ModTable(QTableWidget):
    def __init__(self, parent=None):
        super(ModTable, self).__init__(0, 5, parent)
        # Setup the horizontal label headers.
        self.setHorizontalHeaderLabels(["Mod Name", "Mod Author", "Version", "Update", "Link"])
        
        # Define how the columns work.
        self.modsHeader = self.horizontalHeader() 
        self.modsHeader.setSectionResizeMode(0, QHeaderView.Stretch)
        self.modsHeader.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.modsHeader.setSectionResizeMode(2, QHeaderView.ResizeToContents)

        # Adjust how the elements change in size when window size is reduced / increased.
        self.modsHeader.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        # Counter for bottom of table.
        self.bottom = 0

    def addMod(self, mod):
        self.insertRow(self.bottom)
        self.setItem(self.bottom, 0, QTableWidgetItem(mod.name))
        self.setItem(self.bottom, 1, QTableWidgetItem(mod.author))
        self.setItem(self.bottom, 2, QTableWidgetItem(mod.version))
        self.setItem(self.bottom, 3, QTableWidgetItem("No"))
        self.setItem(self.bottom, 4, QTableWidgetItem(mod.link))
        self.bottom+=1

class PluginTable(QTableWidget):
    def __init__(self, parent=None):
        super(PluginTable, self).__init__(0, 2, parent)
        self.setHorizontalHeaderLabels(["Name", "Enabled"])
        self.pluginsHeader = self.horizontalHeader()
        self.pluginsHeader.setSectionResizeMode(0, QHeaderView.Stretch)
        self.pluginsHeader.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.pluginsHeader.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.bottom = 0

    def addPlugin(self, plugin):
        self.insertRow(self.bottom)
        self.setItem(self.bottom, 0, QTableWidgetItem(plugin.name))
        self.setItem(self.bottom, 1, QTableWidgetItem(plugin.enabled))
        self.bottom+=1


class DownloadTable(QTableWidget):
    def __init__(self, parent=None):
        super(DownloadTable, self).__init__(0, 2, parent)
        self.setHorizontalHeaderLabels(["Name", "Progress"])
        self.downloadsHeader = self.horizontalHeader()
        self.downloadsHeader.setSectionResizeMode(0, QHeaderView.Stretch)
        self.downloadsHeader.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.downloadsHeader.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.bottom = 0

    def addDownload(self, download):
        self.insertRow(self.bottom)
        self.setItem(self.bottom, 0, QTableWidgetItem(str(download.fileID)))
        self.setItem(self.bottom, 1, QTableWidgetItem(download.fileURL))
        self.bottom+=1
