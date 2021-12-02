import sys

from UIManager import UIManager
import PrintMSG

PrintMSG.PrintMSG("Major Python version: %d" % sys.version_info.major)

uiManager = UIManager("Sound SW")

uiManager.start()
