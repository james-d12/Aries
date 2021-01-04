import sys
import Data
from data.NexusAPI import *
from data.NexusKey import NexusKey
from data.Mod import Mod
from data.Download import Download
from gui.App import App
from gui.Window import Window

from gui.settings.SettingsMenu import *

from data.DownloadManager import *

def main():
    nm = NexusKey()
    nm.connect()
    Data.apikey = nm.key
    print(Data.apikey)

    app = App()
    window = Window()

    window.start()

    window.update()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()