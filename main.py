from decimal import MIN_EMIN
import sys
from PyQt5 import QtWidgets
from View.login import Login

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Login()
    app.exec()