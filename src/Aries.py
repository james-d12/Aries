import sys

import Data
from data.NexusKey import NexusKey
from data.Mod import Mod
from data.Download import Download
from gui.App import App
from gui.Window import Window

modlinks=[
    "https://www.nexusmods.com/skyrimspecialedition/mods/12604"
    #"https://www.nexusmods.com/skyrimspecialedition/mods/266",
    #"https://www.nexusmods.com/skyrimspecialedition/mods/659",
    #"https://www.nexusmods.com/skyrimspecialedition/mods/5804",
    #"https://www.nexusmods.com/skyrimspecialedition/mods/19080",
    #"https://www.nexusmods.com/skyrimspecialedition/mods/3038",
    #"https://www.nexusmods.com/skyrimspecialedition/mods/32444",
    #"https://www.nexusmods.com/skyrimspecialedition/mods/272",
    #"https://www.nexusmods.com/skyrimspecialedition/mods/173",
    #"https://www.nexusmods.com/skyrimspecialedition/mods/164",
    #"https://www.nexusmods.com/skyrimspecialedition/mods/1918",
    #"https://www.nexusmods.com/skyrimspecialedition/mods/2182",
    #"https://www.nexusmods.com/skyrimspecialedition/mods/13048",
    #"https://www.nexusmods.com/skyrimspecialedition/mods/1090",
    #"https://www.nexusmods.com/skyrimspecialedition/mods/2154",
    #"https://www.nexusmods.com/skyrimspecialedition/mods/2424",
    #"https://www.nexusmods.com/skyrimspecialedition/mods/6817",
    #"https://www.nexusmods.com/skyrimspecialedition/mods/17230",
    #"https://www.nexusmods.com/skyrimspecialedition/mods/1187",
    #"https://www.nexusmods.com/skyrimspecialedition/mods/16788",
    #"https://www.nexusmods.com/skyrimspecialedition/mods/11802",
    #"https://www.nexusmods.com/skyrimspecialedition/mods/30872",
    #"https://www.nexusmods.com/skyrimspecialedition/mods/2347",
    #"https://www.nexusmods.com/skyrimspecialedition/mods/16495",
    #"https://www.nexusmods.com/skyrimspecialedition/mods/718",
    #"https://www.nexusmods.com/skyrimspecialedition/mods/6369"
]

app = App()
window = Window()

nm = NexusKey()
nm.connect()
Data.apikey = nm.key

window.start()

if nm.connected:
    for m in modlinks:
        dl = Download(m)
        dl.getInfo()
        window.addDownload(dl)

    for m in modlinks:
        mod = Mod(m)
        mod.getInfo()
        window.addMod(mod)


window.update()
sys.exit(app.exec_())
