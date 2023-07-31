from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget

class VentanaComprobante(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaComprobante, self).__init__(parent)
        uic.loadUi("UI/ventanaComprobante.ui", self)
        self.show()

        # Procesos