import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import utils.handelers.account
from GUI.MainInterface import Ui_MainWindow
from PyQt5 import QtWidgets
from init import create_table

create_table()
app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())