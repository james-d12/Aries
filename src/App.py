
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, QFileInfo

from gui.Window import *
import sys
import time

import Data
from data.NexusKey import NexusKey

from data.Mod import Mod
from data.Download import Download

import qtmodern.styles

class App(QtWidgets.QApplication):
    def __init__(self, left=200, top=200, width=1200, height=800):
        super(App, self).__init__([])
        self.setApplicationDisplayName("Aries")
        qtmodern.styles.light(self)
        self.window = Window(left,top,width,height)
        root = QFileInfo(__file__).absolutePath()
        self.window.setWindowIcon(QIcon(root+'/images/icon-32x32.png'))
        
    def start(self):
        self.window.show()

modlinks=[
    "https://www.nexusmods.com/skyrimspecialedition/mods/12604",
    "https://www.nexusmods.com/skyrimspecialedition/mods/266",
    "https://www.nexusmods.com/skyrimspecialedition/mods/659",
    "https://www.nexusmods.com/skyrimspecialedition/mods/5804",
    "https://www.nexusmods.com/skyrimspecialedition/mods/19080",
    "https://www.nexusmods.com/skyrimspecialedition/mods/3038",
    "https://www.nexusmods.com/skyrimspecialedition/mods/32444",
    "https://www.nexusmods.com/skyrimspecialedition/mods/272",
    "https://www.nexusmods.com/skyrimspecialedition/mods/173",
    "https://www.nexusmods.com/skyrimspecialedition/mods/164",
    "https://www.nexusmods.com/skyrimspecialedition/mods/1918",
    "https://www.nexusmods.com/skyrimspecialedition/mods/2182",
    "https://www.nexusmods.com/skyrimspecialedition/mods/13048",
    "https://www.nexusmods.com/skyrimspecialedition/mods/1090",
    "https://www.nexusmods.com/skyrimspecialedition/mods/2154",
    "https://www.nexusmods.com/skyrimspecialedition/mods/2424",
    "https://www.nexusmods.com/skyrimspecialedition/mods/6817",
    "https://www.nexusmods.com/skyrimspecialedition/mods/17230",
    "https://www.nexusmods.com/skyrimspecialedition/mods/1187",
    "https://www.nexusmods.com/skyrimspecialedition/mods/16788",
    "https://www.nexusmods.com/skyrimspecialedition/mods/11802",
    "https://www.nexusmods.com/skyrimspecialedition/mods/30872",
    "https://www.nexusmods.com/skyrimspecialedition/mods/2347",
    "https://www.nexusmods.com/skyrimspecialedition/mods/16495",
    "https://www.nexusmods.com/skyrimspecialedition/mods/718",
    "https://www.nexusmods.com/skyrimspecialedition/mods/6369"
]

app = App()
nm = NexusKey()
nm.connect()
Data.apikey = nm.key

app.start()

#if nm.connected:
    #for m in modlinks:
    #    dl = Download(m)
    #    dl.getInfo(api_key)
    #    app.window.addDownload(dl)
    #    dl.print()
    #for m in modlinks:
    #    mod = Mod(m)
    #    mod.getInfo(Data.apikey)
    #    app.window.addMod(mod)


app.window.update()
sys.exit(app.exec_())
